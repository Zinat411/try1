import random
def Guess_the_number ():
    print(random.random())
    num = random.randint(1, 10)
    user_num= input("choose a number")
    if num == user_num:
        print("You won!")
    else:
        print("oh No! You  Lost")

   
