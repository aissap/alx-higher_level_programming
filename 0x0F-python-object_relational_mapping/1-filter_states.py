#!/usr/bin/python3


import MySQLdb
import sys

if __name__ == "__main__":
    _, username, password, database = sys.argv

    try:
        connection = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database,
            port=3306
        )

        cursor = connection.cursor()

        cursor.execute("""SELECT * FROM states WHERE name
                        LIKE 'N%' ORDER BY id ASC""")

        for row in cursor.fetchall():
            print(row)

    except MySQLdb.Error as e:
        print("Error connecting to MySQL server:", e)

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
