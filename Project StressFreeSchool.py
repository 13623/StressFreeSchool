import webbrowser
import audioop
import tkinter
import os.path
def main():
    global name
    global profession
    name = input("What is your first name?")
    name = name + input('What is your last name?')+'.txt'  # Name of text file coerced with +.txt
    profession = input("Are you a student or a teacher?")
    test()

def test():
    yourTest = open(name,'w') #initialising the text file to record responses
    responses = {} #creating a dictionary to record responses
    Questions = open(profession+".txt",'r') #opening the text file to read questions from
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
    print (TotalScore)
        
main()