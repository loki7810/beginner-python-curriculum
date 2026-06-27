# Problem 1
# Count and print how many times "Alex" appears in the list.
names = ["Liam", "Alex", "Sophie", "Alex", "Mia"]
print(names)
namescount = names.count("Alex")
print("Alex appered", namescount, "times.")



# Problem 2
# Search for "elephant" in the list and print if it's found.
animals = ["zebra", "giraffe", "lion", "tiger", "elephant"]
print(animals)
found = False
index = -1

for i in range(len(animals)):  # Go through each item in the list
    if animals[i] == "elephant":  # If the current item is apple
        found = True  
        index = i  
        break  

if found == True:
    print("Found elephant at", index)
else:
    print("No elephants in the list")

namescount1 = animals.count("elephant")
if namescount1 > 0:
    print("Found elephant")
else:
    print("No elephants in the list")

if "elephant" in animals:
    print("Found elephant")
else:
    print("No elephant found")

# Problem 3
# Count and print how many scores are 100.
scores = [95, 100, 88, 100, 77, 92]
print(scores)
counter = 0
for i in range(len(scores)):  # Go through each item in the list.
    item = scores[i]
    if item == 100:  # Check if the item is "cat"
        counter = counter + 1  # If the item is "cat", add 1 to the counter
print(counter, "100's")

namescount1 = scores.count(100)
print("Found", namescount1, "100")


# Problem 4
# Search for the color "blue" in the list and print its index if it's found.
colors = ["red", "green", "blue", "yellow"]
print(colors)
if "blue" in colors:
    print("found blue(s)")
else:
    print("blue not found")

index = -1
for i in range(len(colors)):  # Go through each item in the list
    if colors[i] == "blue":  # If the current item is apple
        index = i  
        break  

if index != -1:
    print("Found blue at", index)
else:
    print("No blue in the list")

# Problem 5
# Count and print how many temperatures in the list are below zero.
temperatures = [3, -2, 5, -7, 0, 4, -1]
print(temperatures)
counter = 0
for i in range(len(temperatures)):
    item = temperatures[i]
    if item < 0:
        counter = counter + 1
print(counter, "numbers below 0")

    