from os import getenv
import pymssql
import pico
import time

def KZDB(eletext):

	conn = pymssql.connect(host='.\ADITYA', database='SMART')
	cursor = conn.cursor()
	##    print eletext

	cursor.execute('SELECT [Description],[Proc] FROM KnowledgeZone WHERE KnowledgePoint=%s',
					(eletext))
	for row in cursor:
		desc = row[0]
		proc = row[1]
	##    print row[0]
	##    print row[1]
	#	  print("ID=%s, Pass=%s" % (row['Username'], row['Password']))
	#	  conn.commit()
	##    cursor.execute('SELECT * FROM SMART_Registrations')
	##    for row in cursor:
	##        print row
		
	conn.close()
	return desc,proc

##message = KZDB('Advanced Technologies')
##print message
