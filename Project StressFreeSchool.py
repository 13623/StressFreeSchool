import os.path
import time
from tkinter import *

"""
Main function is to get the user started with the program. This function will ask the user his/her name
and profession, and open/create the text file depending on whether the user already has done the test before
and don't need another file created. And then it will pass the information down to either review or test function. Instaed of having two functions each for student and teacher, it only has one function named stressTest because the two functions will be nearly identical and there is no tangible reason to have the two functions when only one function can do the job and use profesion variable to determine how the test is going to be executed.
"""
def main():
    global name
    global profession
    global yourTest
    name = input("What is your first name? ")    
    name = name + " " + input('What is your last name? ') #This allows me to store first name and last name in a single variable
    if any(char.isdigit() for char in name) == True: #Check if the user typed in a number
        print("That is not your name. Your name doesn't have numbers. Please try again")
        main() #go back to the start
    elif set('[~!@#$%^&*()_+{}":;\']+$').intersection(name): # checks if the user typed in a special character
        print ("You put a special character. That's not your name.")
        main()
    elif name[0] == " " or '  '.join(name.split()) == name.strip(): # Check if the user typed in nothing but space
        print ("It looks wrong. Check if you put space in your name or anything at all.")
        main()
    profession = input("Are you a student or a teacher? ")
    if profession[0] == "s" or profession[0] == "S": #if the first letter is s, assume they meant student
        print("I take it as you meant student")
        profession = "students"
    elif profession[0] == "t" or profession[0] == "T": #if the first letter is t, assume they meant teacher
        print("I take it as you meant teacher")
        profession = "teachers"
    else:
        print("I have no idea what you typed in. Please try again ")
        main()
    try:
        """
        The test file is open in this function because it allows me to direct the user to appropriate function depending on what they want to do, such as reviewing their test or doing it again, if they have already done the test. If it was initialised in stressTest function, it will provide no option for the user to review their existing results.
        """
        yourTest = open(os.path.join(os.getcwd()+"\Database",name +'.txt' ),'r+') #If the person has already done the test and the file is in the database, it will be able to open
        print("We see that you have already done this test. Would you like to try again or just view your previous results?")
        print("By agreeing to try again, you will lose your previous results.")
        againInput = input("Press a to try again and anything else to view your results")
        if againInput == "a":
            yourTest.truncate() #Wipe everything on the text file, to prevent writing things over it
            stressTest()
        else:
            review()
    except: #This means the user hasn't done the test yet therefore no file for him in the database
        yourTest = open(os.path.join(os.getcwd()+"\Database",name +'.txt'),'w') #initialising the text file to record responses
        stressTest()

"""
This function will do the actual test to measure the stress level for the user. It will create an empty dictionary to store 
[question number: response], because dictionary is ideal to store a value which corresponds to another value. And then it will open the list of questions depending on their profession, and using loop, the user will get to response to every question written on the text file, and the reason why it uses loop to do the job is because it makes it efficient, having the least possible amount of code for the job. Their responses will then be recorded both on the dictionary and the text
file. Each response stacks up to total score, which will be later passed onto results function to determine the stress level. The total score will be passed on as a parameter, not global variable because only results function will use the variable therefore no need to waste memory.
"""
def stressTest():
    responses = {} #creating a dictionary to record responses
    Questions = open(os.path.join(os.getcwd()+"\Resources",profession+".txt"),'r') #opening the text file to read questions from
    QuestionNo = 0 #initialising the QuestionNo variable
    TotalScore = 0 #initialising the TotalScore variable
    for line in Questions:
        print(line) #print each line, whatever the current line variable holds
        QuestionNo = QuestionNo + 1
        print("Rate how relatable the statement is in range between 1 ~ 5, with 1 being never true and 5 being always true")
        while True:
            try: 
                answer = int(input())
                if 0 < answer < 6:
                    break
                else:
                    print("You can only type in an integer between 1 ~ 5.")
            except ValueError:
                print("Type in a number please")     
        yourTest.write (line) #write the question in the text file
        yourTest.write (str(answer)) #write the response in the text file, in a number format
        yourTest.write ("\n") #new line
        responses[QuestionNo] = answer #record it in the dictionary
        TotalScore = TotalScore + answer #calculate the total score
    results(TotalScore)

"""
This function will determine the results of the test, using the Totalscore variable which has been
passed onto this function as a parameter. This function will also print appropriate advice for the
status. When it finishes, it goes back to the main menu so that another test could be done
Here the pause between the lines of advice is the length of the line divided by 12 so it stops for a brief second to
give the user a sufficient amount of time to read them. It is set to 12 after a comprehensive test of how fast humans
are capable of reading.
"""
def results(TotalScore):
    print ("Hi {0}!".format(name))
    print ("You said you are a {0}, and now the results are here!".format(profession))
    if profession == "students":
        if TotalScore < 99:
            status = "normal"
        elif 131 > TotalScore > 99:
            status = "low"
        elif 172 > TotalScore > 131:
            status = "moderate"
        else:
            status = "high"
    elif profession == "teachers":
        if TotalScore < 60:
            status = "normal"
        elif 81 > TotalScore > 61:
            status = "low"
        elif 110 > TotalScore > 82:
            status = "moderate"
        else:
            status = "high"
    advice = open(os.path.join(os.getcwd()+"\Resources",status+'.txt'),'r') #advice is recorded on a text file
    for line in advice:
        print (line)
        yourTest.write(line)
        time.sleep(len(line)/12) #wait total characters/12 seconds to give the user a bit of time to read before it prints the next line
    yourTest.close()
    print("Going Back to main menu")
    main()

"""
this function is to convert numeric responses to human readable text, because the user's response is
recorded as a number in the text file, and when the user reviews their results in the function review,
the program needs to convert it to understandable format. It is done in a form of a function because 
it is frequently used in review function and to minimise repetition in my code.
"""
def responseConvert(response): #this function is to convert numeric responses to human readable text
    if response == 5:
        print("You said it is always true")
    elif response == 4:
        print("You said it is mostly true")
    elif response == 3:
        print("You said it is quite true")
    elif response == 2:
        print("You said it is occasionally true")
    elif response == 1:
        print("You said it is never true")    

"""
This function is where the user can view their previous results if they have done the test already.
It provides an option for the user whether to view the whole results or specific question. 
After that, it either goes back to the start of the function or the main menu. This is because the user can possibly want to
view their results again or if they decided to view their respones for a specific question, they might want to view another question.
"""
def review():
    print("Your can either view the whole test or your answer to a specific question.")
    reviewOption = input("press w for the whole test, s for specific question")
    if reviewOption.lower() == "w":
        for line in yourTest:
            try:
                responseConvert(int(line)) # checks if the line is a number, in which case it would be response and if so, send it to responseConvert function
                print("\n")
                time.sleep(0.5) #a bit of time for the user to read
            except: #if the line is question, just read it out              
                print(line) 
                time.sleep(0.5) 
        print("Going back to main menu")
        main()
    elif reviewOption.lower() == "s": #S or s, the same
        while True:
            try:    
                QuestionNo = int(input("Please type in the number of question you would like to review: "))
                i = 1
                for line in yourTest:
                    if i == QuestionNo*2-1: #the question is in lines of odd numbers, 13 will be where 7th question is located
                        print (line)
                    elif i == QuestionNo*2:
                        responseConvert(int(line)) #the response to the question is in the next line, sending the integer to response conver function
                    i += 1 #keeps checking the line until it is the line the user is looking for
                break
            except ValueError: #user didn't type in an integer
                print("You didn't type in an integer, please try again")
        print("Going back to start menu")
        main()
        
    else:
        print("W or S please")
        review()
        
main()