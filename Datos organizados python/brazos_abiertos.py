import MySQLdb

db = MySQLdb.connect('127.0.0.1', 'root', '12345', 'body-db')
cursor = db.cursor()
result = cursor.execute("SELECT gesto,headx, heady, headz, neckx, necky, neckz, hipleftx, hiplefty, hipleftz, footleftx, footlefty,"
                        "footleftz, handleftx, handlefty, handleftz,hiprightx, hiprighty, hiprightz, kneeleftx, kneelefty, kneeleftz,"
                        "spinemidx, spinemidy, spinemidz, ankleleftx, anklelefty, ankleleftz, elbowleftx, elbowlefty,elbowleftz, footrightx,"
                        "footrighty, footrightz, handrightx, handrighty, handrightz, kneerightx, kneerighty, kneerightz, spinebasex, spinebasey,"
                        "spinebasez,thumbleftx, thumblefty, thumbleftz, wristleftx, wristlefty, wristleftz, anklerightx, anklerighty, anklerightz,"
                        "elbowrightx, elbowrighty, elbowrightz, thumbrightx,thumbrighty, thumbrightz, wristrightx, wristrighty, wristrightz, "
                        "handtipleftx, handtiplefty, handtipleftz, handtiprightx, handtiprighty, handtiprightz, shoulderleftx,shoulderlefty, "
                        "shoulderleftz, shoulderrightx, shoulderrighty, shoulderrightz, spineshoulderx, spineshouldery, "
                        "spineshoulderz FROM frame WHERE gesto = 'brazos abiertos'")

archivo = open('C:\Users\MCC1\conexionbdb\BrazosAbiertosconsulta.txt', 'a') #CONSULTA
archivito = open('C:\Users\MCC1\conexionbdb\Brazos_Abiertos.txt', 'a')

#########    recorrer la consulta
'''
registro = cursor.fetchall()
for i in registro:
    archivo.write(str(i))
#    print i
#print
registro = cursor.fetchall()
'''
##########   recorre lineas del texto

for line in open('BrazosAbiertosconsulta.txt'):
    M = line.replace("(", " ").replace(")", "\n").lstrip(" ")
    print M

    archivito.write(str(M))


cursor.close()
db.close()

