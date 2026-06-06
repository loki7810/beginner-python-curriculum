# Problem 1
# Ask user for two test scores.
# If BOTH scores are at least 50, print "You passed both!"
# Otherwise, print "You failed at least one."
test = int(input("Give me a test score "))
secondtest = int(input("Give me another test score "))
if test >= 50 and secondtest >= 50:
    print("You passed both !")
else:
    print("you failed at least one")


# Problem 2
# Ask user if they brought lunch and water (yes/no).
# If they brought lunch OR water, print "You're somewhat ready."
# If they brought both, print "You're fully ready!"
# If they brought neither, print "You're not ready."
brought_lunch = input("did you bring lunch (yes/no) ")
brought_water = input("did you bring water (yes/no) ")
if brought_lunch == "yes" or brought_water == "yes":
    print("You are somewhat ready")
if brought_lunch == "yes" and brought_water == "yes":
    print("You are fully ready")
if brought_lunch == "no" and brought_water == "no":
    print("You are not ready")


# Problem 3
# Ask user to enter a number.
# If the number is NOT between 1 and 10 (inclusive), print "Out of range."
# Otherwise, print "In range."
number =int(input("Enter a number "))
if not (number >= 1 and number <= 10):
#if number < 1  and number > 10: 
    print("Out of range")
else:
    print("In range")

# Problem 4
# Generate a random number between 1 and 10.
# Ask the user to guess.
# If the guess is right AND the number is even, print "Even match!"
# Else if guess is right OR number is 5, print "Nice try!"
# Otherwise, print "Nope."
import random # must import the random moudle to use random
num=random.randint(1, 10) # first and last means the boundries for the random number.
numb = int(input("I am guessing a number from 1 to 10. You have 1 try to get it right "))
if num == numb and num % 2 == 0:
    print("Even match")
elif num == numb or numb == 5:
    print("Nice try")
else:
    print("Nope")

# Problem 5
# Ask the user for two numbers.
# If one is divisible by 5 AND the other is NOT divisible by 2, print "Interesting pair!"
# Otherwise, print "Plain pair."
n1 =int(input("Enter a number "))
n2 =int(input("Enter a number "))
if n1 % 5 == 0 and not (n2 % 2 == 0):
    print("interesting pair !")
else:
    print("plain pair.")
