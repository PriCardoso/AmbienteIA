CREATE TABLE hello_world (lang VARCHAR(5), description VARCHAR(200) )

INSERT INTO hello_world ( lang, description) VALUES ('','')

-- Criação do usuário
CREATE USER hello_world WITH
    LOGIN
    NOSUPERUSER
    INHERIT
    NOCREATEDB
    NOCREATEROLE
    NOREPLICATION
    ENCRYPTED PASSWORD 'hello_world';

-- Dá ao usuário permissão para criar bancos de dados
ALTER USER hello_world CREATEDB;

-- Criação do banco de dados
CREATE DATABASE hello_world_db
    WITH 
    OWNER = hello_world
    ENCODING = 'UTF8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

-- Dar permissoes

GRANT ALL PRIVILEGES ON TABLE hello_world TO seu_usuario;
