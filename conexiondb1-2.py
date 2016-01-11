
import MySQLdb
import json

from pprint import pprint

archivo = open('C:\Users\Lucy\Documents\carpeta_vac\Con-Python-Mysql\Archivo.txt' , 'a')

db = MySQLdb.connect('127.0.0.1', 'root', '12345', 'body-db0')

cursor = db.cursor()

result = cursor.execute("SELECT * FROM tbody2")
# x = ('{"head": {"X": -0.3589061, "Y": -0.221765742, "Z": 2.536945}, "neck": {"X": -0.331956834, "Y": -0.327555835, "Z": 2.487806}, "hipLeft": {"X": -0.293213248, "Y": -0.9031639, "Z": 2.28431225}, "footLeft": {"X": -0.162359416, "Y": -0.8145422, "Z": 1.4304471}, "handLeft": {"X": -0.5928216, "Y": -0.5189821, "Z": 2.1657927}, "hipRight": {"X": -0.131359711, "Y": -0.851354957, "Z": 2.19770074}, "kneeLeft": {"X": -0.194363311, "Y": -0.7576734, "Z": 1.79400706}, "spineMid": {"X": -0.275606573, "Y": -0.606517732, "Z": 2.3900485}, "ankleLeft": {"X": -0.241471887, "Y": -0.922651231, "Z": 1.54037118}, "elbowLeft": {"X": -0.404427439, "Y": -0.564060152, "Z": 2.21639156}, "footRight": {"X": -0.09604673, "Y": -1.64478052, "Z": 2.1318903}, "handRight": {"X": -0.08632485, "Y": -0.368517756, "Z": 1.57011688}, "kneeRight": {"X": -0.09191183, "Y": -1.1902895, "Z": 2.20354319}, "spineBase": {"X": -0.2159146, "Y": -0.8908512, "Z": 2.276674}, "thumbLeft": {"X": -0.5796743, "Y": -0.514391065, "Z": 2.13166118}, "wristLeft": {"X": -0.597017348, "Y": -0.52337873, "Z": 2.18530059}, "ankleRight": {"X": -0.0499820076, "Y": -1.58153915, "Z": 2.24445653}, "elbowRight": {"X": -0.214701712, "Y": -0.405588746, "Z": 2.11354065}, "thumbRight": {"X": -0.117162488, "Y": -0.450206816, "Z": 1.58785737}, "wristRight": {"X": -0.152320877, "Y": -0.392675638, "Z": 1.841669}, "handTipLeft": {"X": -0.6152959, "Y": -0.5175693, "Z": 2.16781783}, "handTipRight": {"X": -0.0816261247, "Y": -0.374591, "Z": 1.51953}, "shoulderLeft": {"X": -0.4322195, "Y": -0.4569759, "Z": 2.437166}, "shoulderRight": {"X": -0.272067755, "Y": -0.421932548, "Z": 2.356763}, "spineShoulder": {"X": -0.318280965, "Y": -0.396886349, "Z": 2.465945}}',)

row = cursor.fetchone()

for row in cursor.fetchall():
    y = json.dumps(row)
    z = json.loads(y)
    archivo.write(str(z))
 
cursor.close()
db.close()

