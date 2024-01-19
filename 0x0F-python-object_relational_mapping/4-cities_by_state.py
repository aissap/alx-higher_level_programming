#!/usr/bin/python3
import MySQLdb
import sys


if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = database.cursor()

    query = """
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC
            """

    cursor.execute(query)
    result_rows = cursor.fetchall()
    for row in result_rows:
        print("({}, '{}', '{}')".format(row[0], row[1], row[2]))

    cursor.close()
    database.close()
