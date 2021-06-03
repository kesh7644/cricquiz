 if user_answers =='a' or user_answers == 'b' or user_answers == 'c' or user_answers == 'd':
            if user_answers == answer:
                print("***************************")
                print("nice you got it right ")
                print("***************************")
                score +=1
                print("=======")
                print("your score is",score)
                print("=======")
            else:
                print("**********************************************************")
                print("oops the answer you have chosen is not correct. The right answer is ",answer)    
                print("**********************************************************")
                print("=======")
                print("your score is",score)
                print("=======")


            del questions[0]
            r-=1
            break
        else:
            print("please enter the alphabet for the chosen option")
