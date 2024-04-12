#!/usr/bin/python3
"""Lists all cities within a specified state from the hbtn_0e_4_usa database.

Connects to the database, retrieves cities based on the provided state name
(case-sensitive), and prints a comma-separated list of city names.

Usage: script.py <username> <password> <state_name>
"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.name\
                FROM cities LEFT JOIN states\
                ON states.id = cities.state_id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC", (sys.argv[4],))
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))
    cur.close()
    db.close()
