import webbrowser
import audioop
import tkinter
import os.path
import time
def main():
    global name
    global profession
    global yourTest
    name = input("What is your first name?")    
    name = name + " " + input('What is your last name?')
    if any(char.isdigit() for char in name) == True: #Check if the user typed in a number
        print("That is not your name. Your name doesn't have numbers. Please try again")
        main()
    elif set('[~!@#$%^&*()_+{}":;\']+$').intersection(name): # checks if the user typed in a special character
        print ("You put a special character. That's not your name.")
        main()
    elif name[0] == " " or '  '.join(name.split()) == name.strip(): #Check if the user typed in nothing but space
        print ("It looks wrong. Check if you put space in your name or anything at all.")
        main()
    profession = input("Are you a student or a teacher?")
    if profession[0] == "s" or profession[0] == "S":
        print("I take it as you meant student")
        profession = "students"
    elif profession[0] == "t" or profession[0] == "T":
        print("I take it as you meant teacher")
        profession = "teachers"
    else:
        profession = print("I have no idea what you typed in. Please try again ")
        main()
    try:
        yourTest = open(os.path.join(os.getcwd()+"\Database",name +'.txt' ),'r+') #If the person has already done the test and the file is in the database, it will be able to open
        print("We see that you have already done this test. Would you like to try again or just view your previous results?")
        print("By agreeing to try again, you will lose your previous results.")
        againInput = input("Press a to try again and anything else to view your results")
        if againInput == "a":
            yourTest.truncate() #Wipe everything on the text file, to prevent writing things over it
            test()
        else:
            review()
    except FileNotFoundError: #This means the user hasn't done the test yet therefore no file for him in the database
        yourTest = open(os.path.join(os.getcwd()+"\Database",name +'.txt'),'w') #initialising the text file to record responses
        test()

def test():
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
                if answer < 6 and answer > 0:
                    break
                else:
                    print("You can only type in an integer between 1 ~ 5.")
            except ValueError:
                print("You didn't type in a number. Please try again")     
        yourTest.write (line)
        yourTest.write (str(answer))
        yourTest.write ("\n")
        responses[QuestionNo] = answer
        TotalScore = TotalScore + answer
    print (TotalScore)
    results(TotalScore)

def results(TotalScore):
    print ("Hi {0}!".format(name))
    print ("You said you are a {0}, and now the results are here!".format(profession))
    if profession == "students":
        if TotalScore < 99:
            status = "normal"
        elif TotalScore > 99 and TotalScore < 131:
            status = "low"
        elif TotalScore > 131 and TotalScore < 177:
            status = "moderate"
        else:
            status = "high"
    elif profession == "teachers":
        if TotalScore < 60:
            status = "normal"
        elif TotalScore > 61 and TotalScore < 81:
            status = "low"
        elif TotalScore > 82 and TotalScore < 110:
            status = "moderate"
        else:
            status = "high"
    advice = open(os.path.join(os.getcwd()+"\Resources",status+'.txt'),'r')
    for line in advice:
        print (line)
        yourTest.write(line)
        time.sleep(len(line)/12) #wait total characters/12 seconds to give the user a bit of time to read before it prints the next line
    yourTest.close()
    print("Going Back to main menu")

def review():
    print("Your can either view the whole test or your answer to a specific question.")
    reviewOption = input("press w for the whole test, s for specific question")
    if reviewOption.lower() == "w":
        for line in yourTest:
            try:
                line = int(line)
                if line == 5:
                    print("You said it is always true")
                elif line == 4:
                    print("You said it is mostly true")
                elif line == 3:
                    print("You said it is quite true")
                elif line == 2:
                    print("You said it is occasionally true")
                elif line == 1:
                    print("You said it is never true")
                print("\n")
            except:              
                print(line)
        print("Going back to main menu")
        main()
    elif reviewOption.lower() == "s":
        print("later")
    else:
        print("W or S please")
        review()
        
            
            
    
main()