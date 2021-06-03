#Ask for name by using greet function
def greet():
    global name
    while True:
        name = input("Please enter your name : ")
        if name.isalpha():
            break
        print("Please enter your name in alphabets only.")
greet()#calling the greet function
