__author__ = 'MCC1'

import MySQLdb
import json


db = MySQLdb.connect('127.0.0.1', 'root', '12345', 'body-db0')

cursor = db.cursor()

# ejecutar una consulta

result = cursor.execute("SELECT lectura FROM tbody2")

result_string = json.load(result)
print 'ENCODED:', result_string

decoded = json.load(result_string)
print 'DECOCED:', decoded

#cursor.fetchall()



cursor.close()

db.close()
