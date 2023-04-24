#!/bin/bash
print_red() {
    echo -e "\e[91m$1\e[39m"
}

print_green() {
    echo -e "\e[92m$1\e[39m"
}

print_yellow() {
    echo -e "\e[93m$1\e[39m"
}
if [ "$EUID" -ne 0 ]; then
    print_red "Please run this script with superuser privileges"
    exit 1
fi

dnf update -y
dnf install -y epel-release
dnf install -y vim wget dialog expect

form_new_users="$(dialog --inputbox "Enter a list of users to create (space delimited)" 20 70 "" 3>&1 1>&2 2>&3)" || {
    clear
    exit
}
form_ftp_users="$(dialog --inputbox "Add users allowed to ftp into the server (space delimited)" 20 70 "" 3>&1 1>&2 2>&3)" || {
    clear
    exit
}
form_users_password="$(dialog --inputbox "Add a default password for the new users" 20 70 "" 3>&1 1>&2 2>&3)" || {
    clear
    exit
}
new_users=($form_new_users)
ftp_users=($form_ftp_users)
users_password=$form_users_password

if [[ ! getenforce == "Enforcing" ]]; then
    setenforce 1
fi
for username in "${new_users[@]}"; do
    if ! id -u ${username} >/dev/null 2>&1; then
        adduser ${username}
        usermod -aG wheel ${username}
        passwd --stdin ${username} <<<${users_password}
        print_green "${username} created with password: ${users_password}"
    else
        print_red "${username} already exists."
    fi
done

dnf install -y vsftpd openssl
systemctl enable --now vsftpd

firewall-cmd --zone=public --permanent --add-port=20-21/tcp
firewall-cmd --zone=public --permanent --add-port=30000-31000/tcp
firewall-cmd --zone=public --permanent --add-service=ftp
firewall-cmd --reload

for user in "${ftp_users[@]}"; do
    echo ${user} >>/etc/vsftpd/user_list
done

#sed -i 's/#chroot_local_user=YES/chroot_local_user=YES/g' /etc/vsftpd/vsftpd.conf
echo "local_root=/" >>/etc/vsftpd/vsftpd.conf
echo "dirlist_enable=NO" >>/etc/vsftpd/vsftpd.conf
echo "allow_writeable_chroot=YES" >>/etc/vsftpd/vsftpd.conf
echo "pasv_min_port=30000" >>/etc/vsftpd/vsftpd.conf
echo "pasv_max_port=31000" >>/etc/vsftpd/vsftpd.conf
echo "userlist_file=/etc/vsftpd/user_list" >>/etc/vsftpd/vsftpd.conf
echo "userlist_deny=NO" >>/etc/vsftpd/vsftpd.conf

semanage boolean -m ftpd_full_access --on

echo "ssl_enable=YES" >>/etc/vsftpd/vsftpd.conf
sudo openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -keyout /etc/vsftpd.pem -out /etc/vsftpd/vsftpd.pem
echo "rsa_cert_file=/etc/vsftpd/vsftpd.pem" >>/etc/vsftpd/vsftpd.conf
echo "rsa_private_key_file=/etc/vsftpd.pem" >>/etc/vsftpd/vsftpd.conf

systemctl restart vsftpd || systemctl reload vsftpd
clear

print_green "Successfully configured VSFTPD, new users and enabled users to FTP into this server."
