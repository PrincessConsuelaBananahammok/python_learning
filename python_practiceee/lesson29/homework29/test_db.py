import os
import time

import psycopg2


time.sleep(10)

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT")
)

cursor = conn.cursor()

print("Connected to the database!")


cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        age INTEGER
    )
""")

conn.commit()


# INSERT
cursor.execute("""
    INSERT INTO users (name, age)
    VALUES ('Naruto', 15)
""")

conn.commit()

print("User inserted!")


# SELECT
cursor.execute("SELECT * FROM users")

users = cursor.fetchall()

print("Users:", users)


# UPDATE
cursor.execute("""
    UPDATE users
    SET age = 16
    WHERE name = 'Naruto'
""")

conn.commit()

print("User updated!")


# DELETE
cursor.execute("""
    DELETE FROM users
    WHERE name = 'Naruto'
""")

conn.commit()

print("User deleted!")


cursor.close()
conn.close()