#!/usr/bin/python3
""" lists all states from hbtn_0e_0_usa """
if __name__ == '__main__':
    import MySQLdb
    import sys

    connection = MySQLdb.connect(host="localhost",
                                 port=3306,
                                 user=sys.argv[1],
                                 passwd=sys.argv[2],
                                 db=sys.argv[3],
                                 charset="utf8")
    cur = connection.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)

    connection.close()
    cur.close()
    sys.exit()
