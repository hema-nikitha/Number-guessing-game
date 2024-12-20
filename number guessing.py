import random
range=input("Enter the number for range")
if range.isdigit():
    range=int(range)
    if range<0:
        print("enter the number greater than 0")
        quit()
else:
        print("Continue for next turn")
        quit()
random_number=random.randint(0, range)
guess=0
while True:
    guess+=1
    user=input("Guess the number")
    if user.isdigit():
        user=int(user)
    else:
        print("Come next time")
        continue
    if user==random_number:
        print("Your guess was right")
    elif(user>random_number):
        print("your number was greater than random num")
    else:
        print("your guess was less than random num")
    print("you made", guess, "guesses")         

        
                  