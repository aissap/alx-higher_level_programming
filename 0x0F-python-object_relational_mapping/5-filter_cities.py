#!/usr/bin/python3
import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database_name, state_name = sys.argv[1:5]

    database = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database_name, port=3306)

    cursor = database.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name \
                    FROM cities \
                    JOIN states ON cities.state_id = states.id \
                    WHERE states.name = %s \
                    ORDER BY cities.id ASC", (state_name,))

    rows = cursor.fetchall()

    cursor.close()
    database.close()

    for row in rows:
        print(row)
