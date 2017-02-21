from os import getenv
import pymssql
import pico
import time
import sqlite3
import datetime

def QuerySearch(squery,sarea,subcat): #search query, subject area, subject category
	conn = sqlite3.connect('Databases/SMART.db')
	cursor = conn.cursor()
	
	args = '%'+squery+'%'
	print sarea
	print subcat
	if sarea == "Subject Area" and subcat == "Sub-Category":
		cursor.execute("SELECT KnowledgePoint FROM KnowledgeZone WHERE KnowledgePoint LIKE ?",(args,))
	elif sarea != "Subject Area" and subcat == "Sub-Category":
		#print '1'
		cursor.execute('''SELECT KnowledgePoint FROM KnowledgeZone WHERE KnowledgePoint LIKE ? AND Subject_Area = ?''',(args,sarea))
	elif sarea == "Subject Area" and subcat != "Sub-Category":
		#print '2'
		cursor.execute("SELECT KnowledgePoint FROM KnowledgeZone WHERE KnowledgePoint LIKE ? AND Parent = ?",(args,subcat))
	else:
		#print '3'
		cursor.execute("SELECT KnowledgePoint FROM KnowledgeZone WHERE KnowledgePoint LIKE ? AND Subject_Area = ? AND Parent = ?",
						(args,sarea,subcat))
		
	# Fetch responses
	all_resp = cursor.fetchall()
	
	conn.close() # Close the connection
	return all_resp # Return all responses for the JS to handle
##
##a = QuerySearch('Scan','Robotics & Automation','Sub-Category')
##print(a)
