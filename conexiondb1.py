

import MySQLdb
#import json


db = MySQLdb.connect('127.0.0.1', 'root', '12345', 'body-db0')

cursor = db.cursor()

result = cursor.execute("SELECT * FROM tbody2 WHERE claveU='4F936A16677548F7B408226F54323881' ")

#tbody = [row[0] for row in cursor.fetchall()]

#lista= json.load('cursor.lectura')

#lista['head', 'neck', 'hipLeft']
row = cursor.fetchone()

for row in cursor.fetchall():
    print row
    row = cursor.fetchone()

#for i in row:
#      print i
row = cursor.fetchone()

#db = MySQLdb.connect('127.0.0.1', 'root', '12345', 'body-db0')

#cursor = db.cursor()

#result = cursor.execute("SELECT * FROM tbody2")

#row = cursor.fetchone()

#while row is not None:
#    print (row)
#    row = cursor.fetchone()





#tbodyr =


#print 'total de datos:|| %s \n' % (tbody)




cursor.close()
db.close()


#tbody = [row[0] for row in cursor.fetchall()]
