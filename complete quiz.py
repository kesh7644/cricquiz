from random import shuffle
print("***************************************************")
print("-----------Welcome to the Quiz---------")
print("***************************************************")
#This is a simple quiz

#Ask for name by using greet function
def greet():
    global name
    while True:
        name = input("Please enter your name : ")
        if name.replace(' ','').isalpha():
            break
        print("Please enter your name in alphabets only.")
greet()#calling the greet function



#Ask for age
while True:
    age = input("Please enter your age : ")
    if age.replace(' ','').isnumeric():
        break
    print("please enter numbers only")



#Ask if they are ready to take the quiz
status = input("Are you ready to take the quiz :{}?: \na. Yes \nb. No \n=>".format( name))


#what if the user is ready
if status == 'yes' or status == 'Yes' or status == 'y' or status == 'Y' or status == 'a' or status == 'A':
    print("Welcome to the quiz.")
else:
    print("thank you trying this quiz ")
    exit()

    
##Asking if user wants instructions
def inst():
    inst = input("do you want to read the instructions if you enter anything except y it will not print the instructions :{}?: \na. Yes \nb. No \n=>")
    if inst == 'yes' or inst == 'Yes' or inst == 'y' or inst == 'Y' or inst == 'a' or inst == 'A':
      
        print("==================================INSTRUCTIONS==========================================")
        print("This quiz will ask you questions about the subject of sports")
        print("There will be one correct answer per question. Each Question will have")
        print("four possible answers for each question.")
        print("========================================================================================")
    else:
        
        print("welcome to the quiz")                    
inst()## calling the functions
## number of questions to be asked
def rounds():
    global r ,total
    while True:
        try:
            r = int(input("\nPlease enter how many rounds you want to play : "))##asking the user how many rounds they want to play
            if 0<r<=10:
                break
            else:
                print("please enter the rounds in 1 to 10 only")
        except:
            print('please enter rounds in numbers only (The max is 10)')


    total = r



rounds()
print("==========================================================================")
#set of questions that are asked
#question 1
## questions and right answers

#initial score
Q1 = 'B'
Q2 = 'B'
Q3 = 'B' 
Q4 = 'B'
Q5 = 'A'


score_points = 10
score = 0
correct=0
incorrect=0
questions=[
[
    "For how many days is a Test match scheduled?",
    {'answer':'b','option':'\na.100 over \nb.5 days \nc.One day \nd.50 overs '}##Q1
    ],

[
    "In which year did Kane williamson became the ODI captain for the first time?",##Q2
    {'answer':'b','option':'\na.2011 \nb.2012 \nc.2013 \nd.2014 '}
    ],


[
    "Which is the only country where Williamson doesn't have a Test century?",
    {'answer':'a','option':'\na.South africa \nb.India \nc.West indies \nd.Pakistan '}##Q3
    ],    
    
[
    "Which batsman started his international cricketing career at the age of 16?",
    {'answer':'b','option':'\na.Suresh raina \nb.Sachin tendulkar \nc.Piyush chawla \nd.Rahul dravid '}##Q4
    ],    
    

[
    "Combined width of the three stumps, including small gaps between them is ?",
    {'answer':'a','option':'\na.9 inches \nb.9.5 inches \nc.10 inches \nd.10.5 inches '}##Q5
    ],    
     


[
    "who captains the mumbai indians team in the ipl ?",
    {'answer':'b','option':'\na.Virat kohli \nb.Rohit sharma \nc.MS Dhoni \nd.DJ Bravo '}##Q6
    ],    
     
[
    "who captains the Royal challengers bangalore team in the ipl ?",
    {'answer':'a','option':'\na.virat kohli \nb.Rohit sharma \nc.MS Dhoni \nd.DJ Bravo '}##Q7
    ],    

[
    "who owns mumbai indians team in the ipl ?",
    {'answer':'c','option':'\na.Virat kohli \nb.Rohit sharma \nc.Mukesh Ambani \nd.Vijay malaya '}##Q8
    ],    
[
    "What is nathan lyons nick name?",
    {'answer':'b','option':'\na.Cheeku \nb.The Goat \nc.Thati \nd.Uso '}##Q9
    ],    
[
    "how many wickets do you need to win a test.",
    {'answer':'d','option':'\na.5 wickets \nb.10 wickets \nc.15 wickets \nd.20 wickets '}##Q10
    ],  
    ]
shuffle(questions)
## score mechanics

while r>0:
    data = questions[0]
    q = data[0]
    data =data[1]
    answer = data['answer']
    option = data['option']

    print(q)
    print(option)
    while True:
        user_answers = input("Please enter your answer here : ").lower().replace(' ','')
        if user_answers =='a' or user_answers == 'b' or user_answers == 'c' or user_answers == 'd':
            if user_answers == answer:
                print("***************************")
                print("nice you got it right ")
                print("***************************")
                score+=1
                correct+=1
                print("=======")
                print("your score is",score)
                print("=======")
                incorrect+=1
            else:
                print("**********************************************************")
                print("oops the answer you have chosen is not correct. The right answer is ",answer)    
                print("**********************************************************")
                print("=======")
                print("your score is",score)
                print("=======")


                print("=======")

            del questions[0]
            r-=1
            break
        else:
            print("please enter the alphabet for the chosen option")
            
                    

 
print("")
print("------------------------------------ QUIZ SUMMARY ---------------------------------------")
print("Thanks for playing", name)
print("Your final score is", score,"out of",total)
print("That means you answered", (round(score/total*100,2)),"% of the questions correctly!")
print("You got", correct, "questions correct")
print("You got", incorrect, "questions incorrect")
exit()
