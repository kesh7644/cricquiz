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
