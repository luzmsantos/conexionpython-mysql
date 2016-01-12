

import MySQLdb
import json


db = MySQLdb.connect('127.0.0.1', 'root', '12345', 'body-db0')

cursor = db.cursor()

result = cursor.execute("SELECT lectura FROM tbody2")

for r in cursor.fetchall():
    x = str(r[0])
    jsn = json.loads(x)
    print jsn
    #row = cursor.fetchone()


#print consulta

obj_head = result['head']
obj_neck = result['neck']
obj_hipleft = result['hipLeft']
obj_footLeft = result['handLeft']
obj_handLeft = result['hipRight']
obj_kneeLeft = result['KneeLeft']
obj_spinemid = result['spineMid']

print obj_head




#for row in cursor.fetchall():
 #   print row
    #row = cursor.fetchone()



cursor.close()
db.close()

