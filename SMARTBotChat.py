# Importing all necessary libraries
from os import getenv
import pymssql
import pico
import time
import sqlite3
import datetime
from difflib import SequenceMatcher

def FAQDynamicResp(query):

        temp_similarity = 0
        sim = 0
        count = 0
        sim_count = 0
        
        conn = sqlite3.connect('Databases/SMART.db')
        cursor = conn.cursor()

        cursor.execute('SELECT Question FROM FAQ')
        all_quests = cursor.fetchall()

        cursor.execute('SELECT Answer FROM FAQ')
        all_ans = cursor.fetchall()
        
        for quest in all_quests:
                print quest
                temp_similarity = SequenceMatcher(None, str(query), str(quest)).ratio()
                print temp_similarity
                if temp_similarity > sim:
                        sim = temp_similarity
                        sim_count = count

                count = count + 1

        print sim
        if sim > 0.5:
                return all_quests[sim_count][0], all_ans[sim_count][0]
        else:
               return 0
        

##reply = FAQDynamicResp('Scanbox')
##print str(reply)


