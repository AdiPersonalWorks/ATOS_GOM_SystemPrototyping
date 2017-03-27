import os
from os import getenv
import pymssql
import pico
import time
import sqlite3
from Tkinter import Tk
from shutil import copyfile
from tkFileDialog import askopenfilename
import datetime


def editElement(KnowPoint):
	conn = sqlite3.connect('Databases/SMART.db')
	cur_datetime = str(datetime.datetime.now())
	cur_datetime = cur_datetime.split(' ')[-2]
	cursor = conn.cursor()
	cursor.execute('SELECT Status,Source,Others_Desc,Keywords,Description,Proc,Causal FROM KnowledgeZone WHERE KnowledgePoint=?',(KnowPoint,))
	for row in cursor.fetchall():
		Status = row[0]
		Source = row[1]
		Others_Desc = row[2]
		Keywords = row[3]
		Description = row[4]
		Proc = row[5]
		Causal = row[6]
		# DescImageURL = (str(row[7]).split('/'))[1]
		# print DescImageURL
		# ProcImageURL = (str(row[8]).split('/'))[1]
		# print ProcImageURL
		# CausalImageURL = (str(row[9]).split('/'))[1]
		# print CausalImageURL
		
	conn.close()
	return Status,Source,Others_Desc,Keywords,Description,Proc,Causal

def EditElement_Sub(descname,KPStatus,KPSource,otherarea,keywordstext,desctext,proctext,causaltext,DescImageURL,ProcImageURL,CausalImageURL):
	conn = sqlite3.connect('Databases/SMART.db')
	cursor = conn.cursor()
	cur_datetime = str(datetime.datetime.now())
	cur_datetime = cur_datetime.split(' ')[-2]
	cursor.execute('UPDATE KnowledgeZone SET Description=?,Proc=?,Causal=?,Status=?,Source=?,Others_Desc=?,Keywords=?,DescImageURL=? ,ProcImageURL=?, CausalImageURL=? WHERE KnowledgePoint=?',
		((desctext),(proctext),(causaltext),(KPStatus),(KPSource),(otherarea),(keywordstext),(DescImageURL),(ProcImageURL),(CausalImageURL),(descname)))
	
	time.sleep(2)
	conn.commit()
	conn.close()
	return 1
	
	

def AddElement(parent,descname,KPStatus,KPSource,otherarea,keywordstext,desctext,proctext,causaltext,DescImageURL,ProcImageURL,CausalImageURL):
	conn = sqlite3.connect('Databases/SMART.db')
	cur_datetime = str(datetime.datetime.now())
	cur_datetime = cur_datetime.split(' ')[-2]
	cursor = conn.cursor()
	cursor.execute('INSERT INTO KnowledgeZone (KnowledgePoint,Parent,Description,Proc,Causal,Status,Source,Others_Desc,Keywords,DescImageURL,ProcImageURL,CausalImageURL) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',
                       ((descname),(parent),(desctext),(proctext),(causaltext),(KPStatus),(KPSource),(otherarea),(keywordstext),(DescImageURL),(ProcImageURL),(CausalImageURL)))
	
	time.sleep(2)
	conn.commit()
	conn.close()
	return 1
##
##msg = AddElement('asdasd','asdasd','asdasd','asdasd','asdasd','asdasd','asdasd','asdasd','asdasd')
##print msg

# INSERT INTO KnowledgeZone VALUES (,?,?,?,,?,,?,,,?,,,,?,?,?)

def ChooseImg(id):
	# Make a top-level instance and hide since it is ugly and big.
	root = Tk()
	root.withdraw()

	# Make it almost invisible - no decorations, 0 size, top left corner.
	root.overrideredirect(True)
	root.geometry('0x0+0+0')

	# Show window again and lift it to top so it can get focus,
	# otherwise dialogs will end up behind the terminal.
	root.deiconify()
	root.lift()
	root.focus_force()

	Tk().withdraw()
	
	filePath = askopenfilename(parent=root)
	root.destroy()
	print filePath
	
	fileName = filePath.rsplit('/')
	print fileName
	
	fileName = (fileName[-1])
	print fileName
	
	cwd = os.getcwd()	
	copyfile(str(filePath), cwd+'\\SMART_Images\\'+fileName)
	
	fileName = fileName.rsplit('/')
	fileName = (fileName[-1])
	return fileName
