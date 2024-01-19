#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = database.cursor()
    search_term = sys.argv[4]
    cursor.execute("SELECT DISTINCT * FROM states \
            WHERE name = %s ORDER BY id ASC", (search_term, ))
    result_rows = cursor.fetchall()
    for row in result_rows:
        print(row)
    cursor.close()
    database.close()
