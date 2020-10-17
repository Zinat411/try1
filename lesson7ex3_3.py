def valid_input(input1):
    if input1 == "boom":
        return True
    else:
        return input1.isdigit()
def check_boom(input1):
    if input1 != "boom":
        print("Game Over - you lose!")
    return

def seven_boom():
    user_turn = True
    for num in range(1,21):
     if user_turn == True:
         x = input("Enter the next number or \"boom\":\n")
         if  valid_input(x) != True:
             user_turn = False
             print("GAME OVER - INVALID INPUT!")
             return
         if num % 7 == 0:
             user_turn = False
             check_boom(x)
         elif "7" in str(num):
             user_turn = False
             check_boom(x)
         else:
             user_turn = False
             if int(x) != num:
              print("GAME OVER - YOU LOSE!")
              return
     else:
         user_turn = True
         if num % 7 == 0:
                print("computer says: Boom")
         else:
                print("computer says: {0}".format(num))
    print("GAME OVER - YOU WIN!")
seven_boom()
