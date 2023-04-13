import random
randNo = random.randint(1,100)
userGuess = None
guesses = 0
while(userGuess!=randNo):
    userGuess = int(input("Enter your guess: "))
    guesses +=1
    if(userGuess==randNo):
        print("You have Guessed right")
        print(f"You have Guessed the right number in {guesses} Guesses")
    else:
        if(userGuess>randNo):
            print("You Guessed it wrong! Enter a Small Number")
        else:
            print("You Guessed it worng! Enter a Larger Number")

with open('hiscore1.txt') as f:
        hiscore1 = int(f.read())

if(guesses<hiscore1):
    print("You Broke the Record! Congrats!!")
    with open('hiscore1.txt','w') as f:
        f.write(str(guesses))