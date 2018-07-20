#!/usr/bin/python3
"""
lists all states from hbtn_0e_0_usa
where name matches argument
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
    cur.execute("SELECT * FROM states\
    WHERE states.name LIKE BINARY \'{}\' ORDER BY id ASC"
                .format(sys.argv[4]))
    states = cur.fetchall()

    for state in states:
        print (state)

    connection.close()
    sys.exit()
