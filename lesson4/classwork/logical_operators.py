age = int(input("Enter age here "))
has_ticket = input("do you have a movie ticket? (yes/no) ")
if age >= 13 and has_ticket == "yes": #AND: both conditions are true
    print("you can enter a p-g 13 movie :)")
else:
    print("Sorry, you can't enter :'(")

has_pass = input("do you have a bus pass ? ")
has_coins = input("Do you have coins ")

if has_pass == "yes" or has_coins == "yes": # or means at least one and and means both
    print("you can ride the bus")
else:
    print("you can't ride the bus :(")

homework_done = input("did you do your homework (yes/no)")
if not homework_done =="yes":
    print("go finish your homework!") # what not does is flips true to flase andfalse to true
else:
    print("good job! you are all done :)")
print("check complete")

# you can combine multiple operators
has_permission = input("do you have a SIGNED permission slip")
has_chaperone= input("do you have a chaperone yes/no")
is_sick = input("are you sick today yes/no")
if has_permission == "yes" and has_chaperone == "yes" and not is_sick == "yes":
    print("you can go on a field trip :)))")
elif is_sick == "yes":
    print("you can stay home for today")
elif has_permission == "yes" or has_chaperone == "yes":
    print("You are almost ready, but you are missing something.")
else:
    print("You need a permission slip and a chaperone.")



   


