from os import getenv
import pymssql
import pico
import time
import sqlite3

def CoachMod(id):
        conn = sqlite3.connect('Databases/SMART.db')
        cursor = conn.cursor()


        cursor.execute('SELECT Module_Name,Topic_Name,Topic_Description,ImageURL,VideoURL FROM Learning_Modules WHERE Module_Number=?',(id,))
        for row in cursor.fetchall():
                modname = str(row[0])
                topname = str(row[1])
                topdesc= (row[2])
                imgurl = str(row[3])
                vidurl= str(row[4])

        return modname,topname,topdesc,imgurl,vidurl
        conn.close()

def Evaluate(cur_level,e_q,m_q,h_q):

	conn = sqlite3.connect('Databases/SMART.db')
	cursor = conn.cursor()
	
	if cur_level==1:
		QuestToGet_ID = str(cur_level)+str(e_q)
		cursor.execute('SELECT Question,Option1,Option2,Option3,Option4 FROM Evaluation WHERE Q_Id=?',(QuestToGet_ID,))
		for row in cursor.fetchall():
			quest = str(row[0])
			op1 = str(row[1])
			op2 = str(row[2])
			op3 = str(row[3])
			op4 = str(row[4])
##		e_q = e_q+1
		return quest,op1,op2,op3,op4,e_q,m_q,h_q

	if cur_level==2:
		QuestToGet_ID = str(cur_level)+str(m_q)
		cursor.execute('SELECT Question,Option1,Option2,Option3,Option4 FROM Evaluation WHERE Q_Id=?',(QuestToGet_ID,))
		for row in cursor.fetchall():
			quest = str(row[0])
			op1 = str(row[1])
			op2 = str(row[2])
			op3 = str(row[3])
			op4 = str(row[4])
##		m_q = m_q+1
		return quest,op1,op2,op3,op4,e_q,m_q,h_q

	if cur_level==3:
		QuestToGet_ID = str(cur_level)+str(h_q)
		cursor.execute('SELECT Question,Option1,Option2,Option3,Option4 FROM Evaluation WHERE Q_Id=?',(QuestToGet_ID,))
		for row in cursor.fetchall():
			quest = str(row[0])
			op1 = str(row[1])
			op2 = str(row[2])
			op3 = str(row[3])
			op4 = str(row[4])
##		h_q = h_q+1
		return quest,op1,op2,op3,op4,e_q,m_q,h_q

	
##msg = Evaluate(1,2,1,1)
##print msg

def CheckAns(user_ans,cur_level,cur_ques,e_q,m_q,h_q,no_of_correct):
        conn = sqlite3.connect('Databases/SMART.db')
        cursor = conn.cursor()
        if (cur_level==1):
                cur_quest = str(cur_level)+str(e_q)
                e_q = e_q + 1
        if (cur_level==2):
                cur_quest = str(cur_level)+str(m_q)
                m_q = m_q+1
        if (cur_level==3):
                cur_quest = str(cur_level)+str(h_q)
                h_q = h_q+1

        cursor.execute('SELECT Answer FROM Evaluation WHERE Q_Id=?',(cur_quest,))
        cor_ans = cursor.fetchone()
        cor_ans = str(cor_ans[0])
        # To check the answer
        # If correct
        if (str(user_ans)==cor_ans):
                no_of_correct = no_of_correct+1
                if (cur_level==1):
                        cur_level = 2
                elif (cur_level==2):
                        cur_level = 3
        else: # If incorrect
                if (cur_level==3):
                        cur_level = 2
                elif (cur_level==2):
                        cur_level = 1

        # For next question
        if cur_level==1:
                QuestToGet_ID = str(cur_level)+str(e_q)
                cursor.execute('SELECT Question,Option1,Option2,Option3,Option4 FROM Evaluation WHERE Q_Id=?',(QuestToGet_ID,))
                for row in cursor.fetchall():
                        quest = str(row[0])
                        op1 = str(row[1])
                        op2 = str(row[2])
                        op3 = str(row[3])
                        op4 = str(row[4])
##                e_q = e_q+1
                return quest,op1,op2,op3,op4,e_q,m_q,h_q,cur_level,no_of_correct

        if cur_level==2:
                QuestToGet_ID = str(cur_level)+str(m_q)
                cursor.execute('SELECT Question,Option1,Option2,Option3,Option4 FROM Evaluation WHERE Q_Id=?',(QuestToGet_ID,))
                for row in cursor.fetchall():
                        quest = str(row[0])
                        op1 = str(row[1])
                        op2 = str(row[2])
                        op3 = str(row[3])
                        op4 = str(row[4])
##                m_q = m_q+1
                return quest,op1,op2,op3,op4,e_q,m_q,h_q,cur_level,no_of_correct

        if cur_level==3:
                QuestToGet_ID = str(cur_level)+str(h_q)
                cursor.execute('SELECT Question,Option1,Option2,Option3,Option4 FROM Evaluation WHERE Q_Id=?',(QuestToGet_ID,))
                for row in cursor.fetchall():
                        quest = str(row[0])
                        op1 = str(row[1])
                        op2 = str(row[2])
                        op3 = str(row[3])
                        op4 = str(row[4])
##                h_q = h_q+1  
                return quest,op1,op2,op3,op4,e_q,m_q,h_q,cur_level,no_of_correct  

##msg = CheckAns(2,1,1,1,1,1,0)
##print msg



                

	
	
	
        


