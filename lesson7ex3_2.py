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
    for num in range(1,21):
        x = input("Enter the next number or \"boom\":\n")
        if  valid_input(x) != True:
            print("GAME OVER - INVALID INPUT!")
            return
        if num % 7 == 0:
            check_boom(x)
        elif "7" in str(num):
            check_boom(x)
        else:
            if int(x) != num:
             print("GAME OVER - YOU LOSE!")
             return
    print("GAME OVER - YOU WIN!")
seven_boom()
