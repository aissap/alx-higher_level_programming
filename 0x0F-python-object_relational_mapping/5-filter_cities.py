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

    # Extract city names from the result rows
    cities_list = [row[0] for row in result_rows]

    # Format the output as a comma-separated string
    cities_str = ', '.join(cities_list)
    print(cities_str)

    cursor.close()
    database.close()
