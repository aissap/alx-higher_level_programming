#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    
    state_name = sys.argv[4]

    query = """
            SELECT cities.name
            FROM cities
            JOIN states ON states.id = cities.state_id
            WHERE states.name = %s
            ORDER BY cities.id ASC
            """

    cur.execute(query, (state_name,))
    rows = cur.fetchall()

    # Extract city names from the result rows
    cities_list = [row[0] for row in rows]

    # Format the output as a comma-separated string
    cities_str = ', '.join(cities_list)
    print(cities_str)

    cur.close()
    db.close()
