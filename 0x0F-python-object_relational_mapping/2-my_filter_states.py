#!/usr/bin/python3
"""Fetches state data by name from a MySQL database.

Usage: script.py <username> <password> <database> <state_name>

Connects to the specified MySQL database, retrieves details for the
state matching the provided name (case-sensitive), and prints the results
in table format.
"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
                ORDER BY states.id ASC".format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
