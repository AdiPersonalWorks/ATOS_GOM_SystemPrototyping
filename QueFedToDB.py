from os import getenv
import pymssql
import pico
import time
import sqlite3
import datetime

def QueFedDB(name,email,sub,desc):
	conn = sqlite3.connect('Databases/SMART.db')
	cursor = conn.cursor()
	cur_datetime = str(datetime.datetime.now())
	
	cursor.execute('INSERT INTO Queries_Feedback VALUES (?,?,?,?,?)',
									((name),(email),(sub),(desc),(cur_datetime)))
	
	conn.commit()
	conn.close()
	return 1

