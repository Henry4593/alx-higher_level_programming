#!/usr/bin/python3
"""Lists all cities and their corresponding states from the hbtn_0e_4_usa
database.

Connects to the database, retrieves city and state data using a left join,
and prints the results in a table-like format.
Usage: script.py <username> <password>
"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities LEFT JOIN states\
                ON states.id = cities.state_id\
                ORDER BY cities.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
