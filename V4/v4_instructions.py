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
inst()
