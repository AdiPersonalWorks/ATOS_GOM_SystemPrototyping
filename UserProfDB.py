from os import getenv
import pymssql
import pico
import time
import sqlite3
import datetime

def UserProfPopulate(curr_username):
	conn = sqlite3.connect('Databases/SMART.db')
	cursor = conn.cursor()
	cursor.execute('SELECT FullName,DOB,Department,Designation,Email,UserAccessLevel,SupervisorName,ProfilePic FROM SMART_Registrations WHERE Username=?',(curr_username,))
	
	for row in cursor.fetchall():
		FullName = row[0]
		DOB = row[1]
		Department = row[2]
		Designation = row[3]
		Email = row[4]
		UserAccessLevel = row[5]
		SupervisorName = row[6]
		ProfilePic = row[7]
	
	conn.close()
	return FullName,DOB,Department,Designation,Email,UserAccessLevel,SupervisorName,ProfilePic

def SubmitEdited(curr_username,fullname,dob,dept,desig,email):
	conn = sqlite3.connect('Databases/SMART.db')
	cursor = conn.cursor()
	cursor.execute('UPDATE SMART_Registrations SET FullName=?,DOB=?,Department=?,Designation=?,Email=? WHERE Username=?',
		((fullname),(dob),(dept),(desig),(email),(curr_username)))
	time.sleep(2)
	conn.commit()
	conn.close()
	return 1
	