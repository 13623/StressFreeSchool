import webbrowser
import audioop
import tkinter
import os.path
def main():
    global name
    global profession
    global yourTest
    name = input("What is your first name?")
    name = name + " " + input('What is your last name?')
    profession = input("Are you a student or a teacher?")
    try:
        yourTest = open(os.path.join(os.getcwd()+"\Database",name +'.txt' ),'r+')
        print("We see that you have already done this test. Would you like to try again or just view your previous results?")
        print("By agreeing to try again, you will lose your previous results.")
        againInput = input("Press a to try again and anything else to view your results")
        if againInput == "a":
            yourTest.truncate()
            test()
        else:
            review(yourTest)
    except FileNotFoundError:
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
        responses[QuestionNo] = answer
        TotalScore = TotalScore + answer
        print (responses)
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
        print("working")
        if TotalScore < 60:
            print("working")
            status = "normal"
        elif TotalScore > 61 and TotalScore < 81:
            print("working")
            status = "low"
        elif TotalScore > 82 and TotalScore < 110:
            print("working")
            status = "moderate"
        else:
            print("working")
            status = "high"
    advice = open(os.path.join(os.getcwd()+"\Resources",status+'.txt'),'r')
    for line in advice:
        print (line)
        yourTest.write(line)
    yourTest.close()
    print("Going Back to main menu")
    
            
            
    
main()