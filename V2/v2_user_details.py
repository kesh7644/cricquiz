print("***********************************************************************************************")
print("Welcome to Cricket Quiz. If you are a lover of Cricket Game, you will enjoy playing this quiz.")
print("***********************************************************************************************")

#Asking for name using isalpha 

while True:
    name = input("Please enter your name : ")
    if name.isalpha():
        print("Hello",name,"Welcome to Cricket Quiz")
        break
    else:
        print("Please enter your name in alphabets only.")
        
