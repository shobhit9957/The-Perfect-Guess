import random
randNumber = random.randint(1,100)
print(randNumber)
userGuess = None
Guesses = 0
while(userGuess != randNumber):
        userGuess = int(input("Enter your guess: "))
        Guesses +=1
        if(userGuess==randNumber):
            print("You guessed it right!")
        else:
            if(userGuess>randNumber):
                print("You guessed it wrong! Enter a Smaller number")
            else:
                print("You guessed it wrong! Enter a Larger number")

print(f"You Guessed the number in {Guesses} guesses.")

with open("hiscore.txt", 'r') as f:
    hiscore = int(f.read())

if(Guesses<hiscore):
    print("You have just broken the high score")
    with open("hiscore.txt", 'w') as f:
        f.write(str(Guesses))