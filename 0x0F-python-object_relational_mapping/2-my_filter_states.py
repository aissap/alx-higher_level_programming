#!/usr/bin/python3
"""
Lists all states with a name matching the provided argument
"""
import MySQLdb
import sys


def filter_states_by_input(username, password, database, state_name):
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    cursor = db.cursor()

    que = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    filter_states_by_input(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
