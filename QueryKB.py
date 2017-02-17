from os import getenv
import pymssql
import pico
import time
import sqlite3
import datetime

def QuerySearch(squery):
	conn = sqlite3.connect('Databases/SMART.db')
	cursor = conn.cursor()
	
	args = ['%'+squery+'%']
	cursor.execute("SELECT KnowledgePoint FROM KnowledgeZone WHERE KnowledgePoint LIKE ?",(args))
	all_resp = cursor.fetchall()
	return all_resp