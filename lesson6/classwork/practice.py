# Problem 1
# Count and print how many time "dog" appears in the list.
pets = ["dog", "cat", "dog", "hamster", "dog", "parrot"]
print(pets)
num_dog = pets.count("dog")
print("There are", num_dog, "dogs.")




# Problem 2
# Count and print how many numbers are odd in the list (a number is odd if it's not divisible by 2).
numbers = [8, 3, 12, 7, 4, 11]
counter = 0
for i in range(len(numbers)):
    item = numbers[i]
    if item:
        print(numbers)





# Problem 3
# Search for "monkey" in the list and print its index if it's found.
zoo = ["lion", "elephant", "monkey", "giraffe", "zebra"]
print(zoo)
counter = 0 
for i in range(len(zoo)):  # Go through each item in the list
    if zoo[i] == "monkey":  # If the current item is apple
        found = True  # Mark as found
        index = i  # Save the index
        break  # Exit the loop after finding
if found == True:
    print("found 1 or more monkey(s)")
else:
    print("no monkey found")






# Problem 4
# Search for 99 in the list and print if it’s found.
numbers = [10, 45, 32, 99, 60, 5]
if 99 in numbers:
    print("found 99")
else:
    print("99 not found")



# Problem 5
# Count and print how many numbers are even in the list (a number is odd if it's divisible by 2).
numbers = [13, 22, 8, 19, 6, 7]
print(numbers)