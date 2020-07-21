import random

ran_num = random.randint(1,20)

print("Welcome to number guessing name.")
print("Guess number between 1 and 50.")

def time():
    num = int(input("Guess : "))

    if num == ran_num:
        print("Congrats, You got it right.")
    else:
        diff = abs(ran_num - num)
        if 3 > diff >= 1 :
            print("Wrong but very close... Try again.")
            time()
        elif 6 > diff >= 3:
            print("Wrong guess but close... Try again.")
            time()
        elif 10 > diff >= 6:
            print("Far. Try again.")
            time()
        else:
            print("Very Far. Try again.")
            time()

time()
