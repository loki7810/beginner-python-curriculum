#if statment : runs only when true!
age = int(input("what is your age? "))
if age >= 18:
    print("you can vote!")
else:
    print("you can't vote :o")
print("vote check complete")
#if/else is to use to choose one of 2 paths
temp = int(input("what is the temperture outside "))
if temp < 10:
    print("its cold, wear a jacket")
else:
    print("no jacket needed")
print("weather check done")
# if /elif/else: handle multiple specific case
grade = int(input("Enter your score out of a 100:"))
if grade >= 90:
    print("you got an a")
elif grade >= 80:
    print("you got a b")
elif grade >= 70:
    print("you got a c")
elif grade >= 60:
    print("you got a d")
else:
    print("you failed bwahahahahahahaha >:)))")
print("grading complete")    


    