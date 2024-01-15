#!/usr/bin/python3
"""
Script that connects to a MySQL server and lists all states from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:4]

    try:
        connection = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database,
            port=3306
        )

        cursor = connection.cursor()

        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("Error connecting to MySQL server:", e)

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
