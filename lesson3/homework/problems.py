# Problem 1
# Ask the user to enter a number.
# Print "Even" if the number is divisible by 2, otherwise print "Odd".
num=int(input("enter a number "))
if num % 2 == 0:
    print("Even")
else:
    print("odd")



# Problem 2
# Ask the user for the day of the week (all lowercase).
# Print "Weekend" if the day is "saturday" or "sunday",
# else print "Weekday".
day=str(input("what day of the week is it?"))
if day == "saturday":
    print("weekend")
elif day == "monday":
    print("weekday")
elif day == "tuesday":
    print("weekday")
elif day == "wenesday":
    print("weekday")
elif day == "thursday":
    print("weekday")
elif day == "Friday":
    print("weekday")
elif day == "saturday":
    print("weekend")
else:
    print("there is no such day ")





# Problem 3
# Generate a random number between 1 and 10 (inclusive).
# Ask the user to guess the number.
# Print "Correct!" if the guess matches the random number, else print "Try again!".
numb = int(input("i am guessing a number from 1 to 10. you have 1 try to get it right"))
import random # must import the random moudle to use random
num=random.randint(1, 10) # first and last means the boundries for the random number.
print(num)
if num == numb:
    print("Correct ")
if num != numb:
        print("Try again! :'()")





# Problem 4
# Ask the user for a positive integer.
# If the number is divisible by 2 and greater than 10, print "Big even number".
# Otherwise print "Number does not meet criteria".



# Problem 5
# Ask the user for two numbers.
# Print which number is larger.
# If the numbers are equal, print "Numbers are equal".