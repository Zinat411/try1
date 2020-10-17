import random
def Guess_the_number ():
    num = random.randint(1, 10)
    user_num= input("choose a number")
    while num != int(user_num):
     if num > int(user_num):
        print("The number you choose is lower than the selected random number")
        user_num= input("choose a number")
        if num == int(user_num):
            print("You Win!")
            break
     else:
        print("The number you choose is gerater than the selected random number")
        user_num= input("choose a number")
        if num == int(user_num):
            print("You Win!")
            break
Guess_the_number()
