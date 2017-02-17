from os import getenv
import pymssql
import pico
import time
import sqlite3

def KZDB(eletext):

	#conn = pymssql.connect(host='.\ADITYA', database='SMART')
	conn = sqlite3.connect('Databases/SMART.db')
	cursor = conn.cursor()
	##    print eletext

	cursor.execute('SELECT Description,Proc,DescImageURL FROM KnowledgeZone WHERE KnowledgePoint=?',(eletext,))
	for row in cursor.fetchall():
		desc = row[0]
		proc = row[1]
		imageurl = row[2]
	##    print row[0]
	##    print row[1]
	#	  print("ID=%s, Pass=%s" % (row['Username'], row['Password']))
	#	  conn.commit()
	##    cursor.execute('SELECT * FROM SMART_Registrations')
	##    for row in cursor:
	##        print row
		
	conn.close()
	return desc,proc,imageurl
##
##message = KZDB('Advanced Technologies')
##print message
