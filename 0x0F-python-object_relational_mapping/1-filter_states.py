#!/usr/bin/python3
""" lists all states from hbtn_0e_0_usa
"""

import MySQLdb
import sys


if __name__ == '__main__':

    connection = MySQLdb.connect(host="localhost",
                                 port=3306,
                                 user=sys.argv[1],
                                 passwd=sys.argv[2],
                                 db=sys.argv[3])
    cur = connection.cursor()
    cur.execute("SELECT * FROM states \
    WHERE name LIKE BINARY 'N%'\
    ORDER BY id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    connection.close()
