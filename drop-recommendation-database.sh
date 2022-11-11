docker exec -i recommendation_recommendation-db_1 psql -h localhost -U recommendation postgres << SQL
-- https://stackoverflow.com/questions/17449420/postgresql-unable-to-drop-database-because-of-some-auto-connections-to-db

REVOKE CONNECT ON DATABASE recommendation FROM public;

SELECT pid, pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE datname = 'recommendation' AND pid <> pg_backend_pid();

drop database recommendation;

create database recommendation;

GRANT CONNECT ON DATABASE recommendation TO public;

SQL
