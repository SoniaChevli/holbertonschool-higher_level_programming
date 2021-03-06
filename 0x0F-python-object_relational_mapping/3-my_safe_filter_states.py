#!/usr/bin/python3
"""
lists all states from hbtn_0e_0_usa
where name matches argument
"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    connection = MySQLdb.connect(host="localhost",
                                 user=sys.argv[1],
                                 passwd=sys.argv[2],
                                 db=sys.argv[3])

    cur = connection.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC",
                (sys.argv[4],))

    states = cur.fetchall()

    for state in states:
        print(state)

    connection.close()
    sys.exit()
