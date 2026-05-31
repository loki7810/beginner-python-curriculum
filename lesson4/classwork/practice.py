# Problem 1
# Ask for age and height.
# If age is at least 10 AND height is at least 120 cm, print "You can ride!"
# Otherwise, print "Sorry, you can't ride."
age = int(input("what is your age???"))
height = int(input("what is your height"))
if age >= 10 and height >= 120:
    print("you can ride")
else:
    print("you can't ride")


# Problem 2
# Generate a random number between 1 and 5.
# Ask the user to guess.
# If they guessed right OR the number is 3, print "Lucky!"
# Otherwise, print "Not today"
numb = int(input("guess a number from 1-5 "))
import random # must import the random moudle to use random
num=random.randint(1, 5) # first and last means the boundries for the random number.
if num == numb or num == 3:
    print("Lucky")
else:
    print("not today !")









# Problem 3
# Ask the user to enter 3 numbers.
# If NOT all of them are even (meaning at least one is odd), print "Odd one detected!"
# Otherwise, print "All even!"
a = int(input(" enter a number"))
b = int(input(" enter a number"))
c = int(input(" enter a number"))
if (not(a % 2 ==0 and b % 2 ==0 and c % 2 == 0)):
    print("odd one detected")
else:
    print("all even")

    


# Problem 4
# Ask if the user has a membership and if they scored 100 points in a game.
# If they have a membership OR scored 100, print "You earned a bonus pass!"
# Otherwise, print "No bonus pass."
has_membership = input("do you have a membership? ")
score = input("did you score 100 points?")
if has_membership == "yes" or score == "yes":
    print("you earned a bonus pass")
else:
    print("no bonus pass")


# Problem 5
# Ask the user for a number.
# If it's divisible by 3 AND (either less than 0 OR greater than 100), print "Weird number!"
# Otherwise, print "Normal number."