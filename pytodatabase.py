from os import getenv
import pymssql
import pico
import time

def RegisDB(UID,Pass,email,phone):

    conn = pymssql.connect(host='.\ADITYA', database='SMART')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO SMART_Registrations VALUES (%s,%s,%s,%s)',
					(UID,Pass,email,phone))
    #for row in cursor:
        #print(row)
        #print("ID=%s, Pass=%s" % (row['Username'], row['Password']))
    time.sleep(5)
    conn.commit()
    time.sleep(5)
##    cursor.execute('SELECT * FROM SMART_Registrations')
##    for row in cursor:
##        print(row)
        
    conn.close()
    return "Successfully Inserted a new record !!"

##message = RegisDB('a1s','a12','aasd','2232')
##print message
