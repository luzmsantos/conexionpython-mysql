__author__ = 'MCC1'

import MySQLdb
import json


db = MySQLdb.connect('127.0.0.1', 'root', '12345', 'body-db0')

cursor = db.cursor()

result = cursor.execute("SELECT claveU FROM tbody2")


tbody = [row[0] for row in cursor.fetchall()]

print 'total de datos: %s' % (tbody)

cursor.close()

db.close()
