# Problem 1
# Ask the user to enter a number.
# Print "Even" if the number is divisible by 2, otherwise print "Odd".
num=int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")



# Problem 2
# Ask the user for the day of the week (all lowercase).
# Print "Weekend" if the day is "saturday" or "sunday",
# else print "Weekday".
day = input("What day of the week is it? ")
if day == "sunday":
    print("Weekend")
elif day == "monday":
    print("Weekday")
elif day == "tuesday":
    print("Weekday")
elif day == "wednesday":
    print("Weekday")
elif day == "thursday":
    print("Weekday")
elif day == "friday":
    print("Weekday")
elif day == "saturday":
    print("Weekend")
else:
    print("there is no day called that ")





# Problem 3
# Generate a random number between 1 and 10 (inclusive).
# Ask the user to guess the number.
# Print "Correct!" if the guess matches the random number, else print "Try again!".
numb = int(input("I am guessing a number from 1 to 10. You have 1 try to get it right "))
import random # must import the random moudle to use random
num=random.randint(1, 10) # first and last means the boundries for the random number.
print(num)
if num == numb:
    print("Correct ")
else:
    print("Try again! :'(")





# Problem 4
# Ask the user for a positive integer.
# If the number is divisible by 2 and greater than 10, print "Big even number".
# Otherwise print "Number does not meet criteria".
i = int(input("Give me an positive interger "))
if i % 2 == 0:
  if i > 10:
    print("Big even number")
  else:
      print("Number does not meet criteria")
else:
    print("Number does not meet criteria ")
    



# Problem 5
# Ask the user -for two numbers.
# Print which number is larger.
# If the numbers are equal, print "Numbers are equal".
a = int(input("Enter a number "))
b = int(input("Enter another number "))
if a > b:
    print( a )
elif b > a:
    print( b )
else:
    print("Numbers are equal")
    
