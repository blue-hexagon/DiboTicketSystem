DROP DATABASE dibo_security;
CREATE USER dibo_admin WITH SUPERUSER ENCRYPTED PASSWORD 'Kode1234!' LOGIN CREATEDB CREATEROLE;
CREATE DATABASE dibo_security WITH OWNER dibo_admin;
SELECT pg_sleep(10); -- Do your thing...
                     -- Run: 'python manage.py migrate'
                     -- Run: 'python manage.py create_users'
                     -- Run: 'python manage.py inspectdb > dirty_models.py' to export models for django


\c dibo_security dibo_admin;
\! chcp 65001
SET CLIENT_ENCODING TO 'UTF-8';
GRANT ALL PRIVILEGES ON DATABASE dibo_security TO dibo_admin;
ALTER ROLE dibo_admin SET client_encoding TO 'UTF-8';
ALTER ROLE dibo_admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE dibo_admin SET timezone TO 'Denmark/Copenhagen';
SET timezone = 'Denmark/Copenhagen';

CREATE TABLE ticket
(
	id          INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	timestamp   TIMESTAMPTZ,
	level       INT NOT NULL CHECK (level >=1 AND level <= 3),
	message	    TEXT NOT NULL,
	user_id     INT NOT NULL,

	FOREIGN KEY (user_id)
		REFERENCES auth_user (id)
		ON DELETE RESTRICT
);

CREATE TABLE logging
(
    id          INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	timestamp   TIMESTAMPTZ,
	level       INT NOT NULL CHECK (level >=1 AND level <= 3),
	message	    TEXT NOT NULL,
	user_id     INT NOT NULL,
);
