from os import getenv
import pymssql
import pico
import time
import sqlite3
import datetime

def RegisDB(Username,Pass,email,dept):

	#conn = pymssql.connect(host='.\ADITYA', database='SMART')
	conn = sqlite3.connect('Databases/SMART.db')
	cursor = conn.cursor()
	cur_datetime = str(datetime.datetime.now())
	usrType = 'Expert'

	try:
		cursor.execute('INSERT INTO SMART_Registrations (Username, Password, Email, Department, UserAccessLevel, CreatedTime, LastLogin) VALUES (?,?,?,?,?,?,?)',
									((Username),(Pass),(email),(dept),(usrType),(cur_datetime),(cur_datetime)))

		time.sleep(5)
		conn.commit()
		time.sleep(5)
		conn.close()
		return 1
	except:
		return 0

# Login Validation
def Login_Validate(UID,Pass):
        users = []
        passwords = []
        conn = sqlite3.connect('Databases/SMART.db')
        cursor = conn.cursor()

        cursor.execute('SELECT Username,Password FROM SMART_Registrations')

        all_usernames = cursor.fetchall()
        print all_usernames
        for user in all_usernames:
                users.append(str(user[0]))
                passwords.append(str(user[1]))

        try:
                index = users.index(UID)
                print index
                if Pass == passwords[index]:
                        print 'Password matched'
                        return 1
                else:
                        return 0
        except:
                #time.sleep(5)
                return 0

        conn.close()

##message = Login_Validate('adityaexpert','adityaexpert')
##print message
	
