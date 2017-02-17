from os import getenv
import pymssql
import pico
import time
import sqlite3
import datetime

def RegisDB(UID,Pass,email,phone):

	#conn = pymssql.connect(host='.\ADITYA', database='SMART')
	conn = sqlite3.connect('Databases/SMART.db')
	cursor = conn.cursor()
	cur_datetime = str(datetime.datetime.now())
	usrType = '1'

	try:
		cursor.execute('INSERT INTO SMART_Registrations VALUES (?,?,?,?,?,?,?)',
									((UID),(Pass),(email),(phone),(usrType),(cur_datetime),(cur_datetime)))

		time.sleep(5)
		conn.commit()
		time.sleep(5)
		conn.close()
		return "y"
	except:
		return "n"
          
# Login Validation
def Login_Validate(UID,Pass):
	print(UID)
	print(Pass)
	conn = sqlite3.connect('Databases/SMART.db')
	cursor = conn.cursor()

	cursor.execute('SELECT * FROM SMART_Registrations WHERE Username=? AND Password=?',
						((UID),(Pass)))
	time.sleep(10)
	retlen = len(cursor.fetchall())
	print(retlen)
	#time.sleep(5)
	if retlen>0:
			conn.close()
			#time.sleep(2)
			time.sleep(10)
			return "y"  
			
	else:
			conn.close()
			#time.sleep(2)
			time.sleep(10)
			return "n"

#message = Login_Validate('adityaexpert','adityaexpert123')
#print message
