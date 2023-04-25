DROP DATABASE dibo_security;
DROP USER dibo_admin;

CREATE USER dibo_admin WITH SUPERUSER ENCRYPTED PASSWORD 'Kode1234!' LOGIN CREATEDB CREATEROLE;
CREATE DATABASE dibo_security WITH OWNER dibo_admin;
GRANT ALL PRIVILEGES ON DATABASE dibo_security TO dibo_admin;
\c dibo_security dibo_admin;
\! chcp 65001
SET CLIENT_ENCODING TO 'UTF-8';

ALTER ROLE dibo_admin SET client_encoding TO 'UTF-8';
ALTER ROLE dibo_admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE dibo_admin SET timezone TO 'Europe/Copenhagen';
SET timezone = 'Europe/Copenhagen';

SELECT pg_sleep(2);
-- Run: 'python manage.py migrate'
-- Run: 'python manage.py create_users'
-- Run: 'python manage.py inspectdb > dirty_models.py' to export models for django



CREATE TABLE ticket
(
	id                  INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	timestamp           TIMESTAMPTZ DEFAULT now(),
	level               INT NOT NULL DEFAULT 1 CHECK (level >= 1 AND level <= 3),
	problem_message	    TEXT NOT NULL,
	status_message      TEXT,
	solution_message    TEXT,
	user_id             INT NOT NULL,
	is_open             BOOLEAN NOT NULL DEFAULT TRUE,

    customer_first_name   VARCHAR(40)            NOT NULL CHECK ( customer_first_name ~ '^[a-zA-ZæøåÆØÅ]{2,}$' ),
    customer_last_name    VARCHAR(40)            NOT NULL CHECK ( customer_last_name ~ '^[a-zA-ZæøåÆØÅ\.\s]{1,}$'),
    customer_phone_number TEXT                   NOT NULL CHECK ( customer_phone_number ~ '^[0-9]{8,8}$' ),
    customer_email        VARCHAR(100)           NOT NULL,

	FOREIGN KEY (user_id)
		REFERENCES auth_user (id)
		ON DELETE RESTRICT
);

CREATE TABLE ticket_log (
    id          INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    timestamp   TIMESTAMPTZ DEFAULT now(),
    action      TEXT NOT NULL,
    table_name  TEXT NOT NULL,
    user_id     INT NOT NULL,
    old_data    JSONB,
    new_data    JSONB
);


-- TG_OP: Contains the operation that triggered the trigger function. Its value can be 'INSERT', 'UPDATE', or 'DELETE'.
-- TG_TABLE_NAME: Cntains the name of the table that triggered the trigger function.
-- NEW: Contains a record that represents the new row being inserted or the updated row after an update operation. Available in trigger functions that are fired after an insert or update operation.
-- OLD: Contains a record that represents the original row being updated or the row being deleted. It is available in trigger functions that are fired after an update or delete operation.
CREATE OR REPLACE FUNCTION ticket_trigger_func()
RETURNS TRIGGER AS $$
BEGIN
    IF (TG_OP = 'INSERT') THEN
        INSERT INTO ticket_log (action, table_name, user_id, new_data)
        VALUES ('INSERT', TG_TABLE_NAME, NEW.user_id, to_jsonb(NEW));
    ELSIF (TG_OP = 'UPDATE') THEN
        INSERT INTO ticket_log (action, table_name, user_id, old_data, new_data)
        VALUES ('UPDATE', TG_TABLE_NAME, NEW.user_id, to_jsonb(OLD), to_jsonb(NEW));
    ELSIF (TG_OP = 'DELETE') THEN
        INSERT INTO ticket_log (action, table_name, user_id, old_data)
        VALUES ('DELETE', TG_TABLE_NAME, OLD.user_id, to_jsonb(OLD));
    END IF;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER ticket_trigger
AFTER INSERT OR UPDATE OR DELETE ON ticket
FOR EACH ROW
EXECUTE FUNCTION ticket_trigger_func();

INSERT INTO ticket (level,is_open, user_id, customer_first_name, customer_last_name, customer_phone_number, customer_email, problem_message)
VALUES
(1, DEFAULT, 1, 'Oscar',   'Petterson',    '29382918', 'ospe@dibo.dk',     'Brugeren er låst ude af sin konto'),
(2, DEFAULT, 1, 'Adam',    'Danielsson',   '92818273', 'adda@dibo.dk',     'Brugerens comptuer er brudt sammen'),
(3, DEFAULT, 2, 'William', 'Meldgaard',    '11827374', 'wime@dibo.dk',     'Brugeren kan ikke åbne sin mail'),
(1, DEFAULT, 2, 'Niels',   'Wallin',       '26273829', 'niwa@dibo.dk',     'Brugeren kan ikke tilkoble sig WiFi'),
(1, DEFAULT, 3, 'Ida',     'Holmberg',     '13627447', 'idho@dibo.dk',     'Brugeren meddeler at hendes touchpad stopper med at virke, hver formiddag efter hun har brugt sin computer et par timer'),
(1, DEFAULT, 3, 'Oscar',   'Lundberg',     '28768744', 'oslu@dibo.dk',     'Brugeren har problemer med Airtame, hun kan ikke tilkoble sig'),
(1, DEFAULT, 4, 'Per',     'Danielsson',   '28727364', 'peda@dibo.dk',     'Brugeren kan ikke forbinde sin computer til Clevershare'),
(3, DEFAULT, 4, 'William', 'Fredriksson',  '43776142', 'wifr@dibo.dk',     'Brugeren meddeler, at han og flere andre lærere på HTX ikke kan komme på internettet. Problemet vedrører ikke lærere på andre afdelinger.');


\c postgres postgres