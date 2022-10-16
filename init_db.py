import os
import psycopg2


def env_or_default(var_name, default):
    environment_variable = os.getenv(var_name)
    if environment_variable:
        return environment_variable
    return default


conn = psycopg2.connect(
    host="localhost",
    database="recommendation",
    user= env_or_default('RECOMMENDATION_DB_USERNAME', "recommendation"),
    password=env_or_default('RECOMMENDATION_DB_PASSWORD','recommendation'))

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS dancer;')
cur.execute('CREATE TABLE dancer (id uuid PRIMARY KEY,'
            'name varchar (150) NOT NULL);'
            )

# Insert data into the table

cur.execute('INSERT INTO dancer (id, name)'
            'VALUES (\'bb30ae5a-4d1f-11ed-b142-67b8c323121c\' , \'marc\')'
            )

conn.commit()

cur.close()
conn.close()
