from os import getenv
import pymssql
import pico
import time
import sqlite3
import datetime

def KM_DB(KnowPoint):
	conn = sqlite3.connect('Databases/SMART.db')
	cursor = conn.cursor()
	
	cursor.execute('SELECT Description,Proc,DescImageURL,Parent,Status,UID,CreatedBy,ModifiedBy,KnowledgeType,Causal FROM KnowledgeZone WHERE KnowledgePoint=?',(KnowPoint,))
	for row in cursor.fetchall():
		desc = row[0]
		proc = row[1]
		imageurl = row[2]
		parent = row[3]
		status = row[4]
		UID = row[5]
		Created = row[6]
		Modified = row[7]
		KType = row[8]
		causal = row[9]
		
	conn.close()
	return desc,proc,imageurl,parent,status,UID,Created,Modified,KType,causal
	
def getParents(KnowPoint):
	conn = sqlite3.connect('Databases/SMART.db')
	cursor = conn.cursor()
	cursor.execute('SELECT Parent FROM KnowledgeZone WHERE KnowledgePoint=?',(KnowPoint,))
	all_resp = cursor.fetchall()
	conn.close()
	return all_resp
	
def getChildren(KnowPoint):
	conn = sqlite3.connect('Databases/SMART.db')
	cursor = conn.cursor()
	cursor.execute('SELECT KnowledgePoint FROM KnowledgeZone WHERE Parent=?',(KnowPoint,))
	all_resp = cursor.fetchall()
	conn.close()
	return all_resp

def DelKnowPoint(KnowPoint):
	conn = sqlite3.connect('Databases/SMART.db')
	cursor = conn.cursor()
	cursor.execute('DELETE FROM KnowledgeZone WHERE KnowledgePoint=?',(KnowPoint,))
	conn.commit()
	conn.close()
	return 1