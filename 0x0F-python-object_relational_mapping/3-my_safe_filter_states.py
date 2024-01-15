#!/usr/bin/python3
import MySQLdb
import sys


def filter_states(username, password, database, state_name):
    try:
        connection = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database,
            port=3306
        )

        cursor = connection.cursor()

        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))

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


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)
        script_name = sys.argv[0]
        print(f"Usage: {script_name} <username> <password> \
                <database> <state_name>")

    filter_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
