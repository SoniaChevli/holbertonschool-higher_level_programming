#!/usr/bin/python3
"""
lists all cities from hbtn_0e_0_usa
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
    cmd = "SELECT cities.id, cities.name, states.name \
    FROM cities JOIN states ON states.id = cities.id"
    cur.execute(cmd)
    cities = cur.fetchall()

    for city in cities:
        print (city)

    connection.close()
    sys.exit()
