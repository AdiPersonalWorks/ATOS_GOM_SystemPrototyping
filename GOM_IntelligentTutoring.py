'''

Intelligent Evaluation System
@author : TEAM
last changed: 16-01-2017
Changelogs:
1) 16-01-2017: Created


'''

# Importing required libraries
import csv
import pandas as pd

quest_list = pd.read_csv("QuestionSet_1.csv") # Change path as required

# Remove all NaN here later


# Variable initializations.
# (Change as required)
easy_quest = 0
med_quest = 5
dif_quest = 10
count = 1
correct = 0 # To keep track of the number of correct answers

# Forming the required arrays
all_questions = quest_list.Question
all_option1 = quest_list.Option1
all_option2= quest_list.Option2
all_option3 = quest_list.Option3
all_option4 = quest_list.Option4
all_answers = quest_list.Answer

level = 1

print("Each question has only one correct answer. Please choose from options 1-4")
print("There will be a total of five questions")
print("All the best !")

for i in range(0,5):

    # For Easy level questions
    if level == 1:
        print("\n")
        print("Question "+str(count)+"-> "+all_questions[easy_quest])
        print("1. "+all_option1[easy_quest])
        print("2. "+all_option2[easy_quest])
        print("3. "+all_option3[easy_quest])
        print("4. "+all_option4[easy_quest])
        val = input("-> ")
        
        count = count + 1
        if val==all_answers[easy_quest]:
            print("Correct Answer!!!")
            level = 2
            correct = correct+1
        easy_quest = easy_quest+1

    # For Medium level questions
    elif level == 2:
        print("\n")
        print("Question "+str(count)+"-> "+all_questions[med_quest])
        print("1. "+all_option1[med_quest])
        print("2. "+all_option2[med_quest])
        print("3. "+all_option3[med_quest])
        print("4. "+all_option4[med_quest])
        val = input("-> ")
        
        count = count + 1
        if val==all_answers[med_quest]:
            print("Correct Answer!!!")
            level = 3
            correct = correct+1
        else:
            level = 1

        med_quest = med_quest+1
        
# For Difficult level questions
    elif level == 3:
        print("\n")
        print("Question "+str(count)+"-> "+all_questions[dif_quest])
        print("1. "+all_option1[dif_quest])
        print("2. "+all_option2[dif_quest])
        print("3. "+all_option3[dif_quest])
        print("4. "+all_option4[dif_quest])
        val = input("-> ")
        
        count = count + 1
        if val==all_answers[dif_quest]:
            print("Correct Answer!!!")
            level = 3
            correct = correct+1
        else:
            level = 2

        dif_quest = dif_quest+1
        
print("\n")
print("You have scored -> "+str(correct)+"/5")
