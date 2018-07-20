#!/usr/bin/python3
"""
lists all cities of the state passed in
"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    connection = MySQLdb.connect(host="localhost",
                                 port=3306,
                                 user=sys.argv[1],
                                 passwd=sys.argv[2],
                                 db=sys.argv[3])

    cur = connection.cursor()
    cmd = "SELECT cities.name FROM cities \
    JOIN states ON states.id = cities.state_id \
    WHERE states.name =%s".format((sys.argv[4],))
    citynum = cur.execute(cmd)
    cities = cur.fetchall()
    for i in range(citynum):
        if i == citynum - 1:
            print(cities[i][0])
        else:
            print(cities[i][0], end=", ")

    cur.close()
    connection.close
    sys.exit()
