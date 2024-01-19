#!/usr/bin/python3
import MySQLdb
import sys


if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = database.cursor()

    state_name = sys.argv[4]

    query = """
            SELECT cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
            """

    cursor.execute(query, (state_name,))
    result_rows = cursor.fetchall()

    cities_list = [row[0] for row in result_rows]
    print(', '.join(cities_list))

    cursor.close()
    database.close()
