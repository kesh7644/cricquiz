print("***************************************************")
print("-----------Welcome to the Quiz---------")
print("***************************************************")
#This is a simple quiz
#initial score
Q1 = 'B'
Q2 = 'B'
Q3 = 'B' 
Q4 = 'B'
Q5 = 'A'

score = 0
#Ask for name
def greet():
    global name
    while True:
        name = input("Please enter your name : ")
        if name.isalpha():
            break
        print("Please enter your name in alphabets only.")
greet()
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

        print("This quiz will ask you questions about the subject of sports")
        print("There will be one correct answer per question. Each Question will have")
        print("four possible answers for each question.")
    else:
        print("welcome to the quiz")
inst()
## number of questions to be asked
def get_range():
    num=int(input("Please enter number of questions you would like to play:"))
    return num
num=get_range() #calling the get range function
#set of questions that are asked
#question 1
## questions and right answers
questions={
    "For how many days is a Test match scheduled?": "5 days",
    "In which year did Kane williamson became the ODI captain for the first time?": "2012",
    "Which is the only country where Williamson doesn't have a Test century?": "South Africa",
    "Which batsman started his international cricketing career at the age of 16?": "Sachin Tendulkar",
    "Combined width of the three stumps, including small gaps between them is ?": "9 inches",
    
    
    


 



    }

##options for the answers
optlist=['100 overs:5days:one day:50 overs',
         '2011:2012:2013:2014',
         'South africa:india:west indies:pakistan',
        'Suresh Raina:Sachin Tendulkr:Piyush chawla: Rahul dravid',
        '9 inches:9.5 inches:10 inches:10.5',
         
         
         
         
         
     





    ]


print("\nQuestion: 1|score:{}".format(score))
ans=input("For how many days is a Test match scheduled\na.100 over \nb.5 days \nc.one day \nd.50 overs Your answer : ")
if ans == '5 days' or ans == '5' or ans =='B' or ans == 'b':
    print("Correct")
    score+=1
    print("Your score is",score)
else:
    print("Oops incorrect the correct answer is :" ,Q1)
    if score <=0:
        score = 0
        print("Your score is",score)

print("\nQuestion: 2|score:{}".format(score))
ans=input("In which year did Kane williamson became the ODI captain for the first time?\na.2011 \nb.2012 \nc.2013 \nd.2014 Your answer : ")
if ans == '2012' or ans == '2012' or ans =='B' or ans == 'b':
    print("Correct")
    score+=1
    print("Your score is",score)
else:
    print("Oops incorrect the correct answer is :" ,Q2)
    if score <=0:
        score = 0
        print("Your score is",score)
            
print("\nQuestion: 3|score:{}".format(score))
ans=input("Which is the only country where Williamson doesn't have a Test century?\na.South africa \nb.india \nc.west indies \nd.pakistan Your answer : ")
if ans == 'south africa' or ans == 'SA' or ans =='B' or ans == 'b':
    print("Correct")
    score+=1
    print("Your score is",score)
else:
    print("Oops incorrect the correct answer is :" ,Q3)
    if score <=0:
        score = 0
        print("Your score is",score)

print("\nQuestion: 4|score:{}".format(score))
ans=input("Which batsman started his international cricketing career at the age of 16?\na.Suresh Raina \nb.Sachin Tendulkr  \nc.Piyush chawla \nd. Rahul dravid Your answer : ")
if ans == 'Sachin tendulkar' or ans == 'Sachin' or ans =='B' or ans == 'b':
    print("Correct")
    score+=1
    print("Your score is",score)
else:
    print("Oops incorrect the correct answer is :" ,Q4)
    if score <=0:
        score = 0
        print("Your score is",score)
    

print("\nQuestion: 5|score:{}".format(score))
ans=input("Combined width of the three stumps, including small gaps between them is ?\na.9 inches \nb.9.5 inches  \nc.10 inches \nd.10.5 inches Your answer : ")
if ans == '9 inches' or ans == '9' or ans =='A' or ans == 'a':
    print("Correct")
    score+=1
    print("Your score is",score)
else:
    print("Oops incorrect the correct answer is :" ,Q5)
    if score <=0:
        score = 0
        print("Your score is",score)



    
            
            
    
