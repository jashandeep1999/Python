import random

def AutoGuess(lowval , highval , randnum, count = 0):
    if highval >=lowval:
        guess = (highval + lowval) // 2
        #then no. is in middle
        if guess == randnum:
            return count
        elif guess > randnum:
            count = count + 1
            AutoGuess(lowval , guess - 1, randnum, count)
        else:
            count = count + 1
            AutoGuess(guess + 1, highval , randnum, count)
    else:
        #number not in range
        return -1
#end of function

#generate a random no. between 1 and 100

randnum = random.randint(1,101)
count = 0
guess = -99

while (guess != randnum):
    #get the user to guess a number
    guess = (int) (input("enter any number from 1 to 100: "))
    if guess < randnum:
        print("lower!")
    elif guess > randnum:
        print("Higher!")
    else:
        print("You guessed it!")
        break
    count = count + 1
#end of while loop

print("took you " + str(count) + " steps to guess.")
print("computer took " + str(AutoGuess(1,100,randnum)) + " steps to guess!!")
