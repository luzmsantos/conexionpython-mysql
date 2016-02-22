import MySQLdb
db = MySQLdb.connect('127.0.0.1', 'root', '12345', 'body-db')
cursor = db.cursor()

archivo = open('C:\Users\MCC1\conexionbdb\Archivo.txt', 'a')
result = cursor.execute("SELECT gesto,headx, heady, headz, neckx, necky, neckz FROM frame WHERE nombre = 'Viridiana'")
cursor1 = cursor.fetchall()

co = cursor.execute("SELECT idlectura FROM frame WHERE gesto = 'brazo arriba'")
cursor2 = cursor.fetchall()

concate = []
for r in cursor1:
    #if r.registro == r.registro:
    for i in r:
        concate.append(i)
print concate

print
cursor1 = cursor.fetchall()
archivo.write(str(concate))


archivo.close()
cursor.close()
db.close()
