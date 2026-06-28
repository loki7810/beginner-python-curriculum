# Problem 1
# Find and print the total sum of all the numbers in the list.
numbers1 = [4, 11, 22, -6, 3]
total = sum(numbers1) # shortcut to find item
print("the sum is", total) 




# Problem 2
# Find and print the biggest number in the list.
numbers2 = [-9, 17, 5, -3, 0]
biggestitem = max(numbers2)
print("the biggest item is", biggestitem)


# Problem 3
# Find and print the sum of only the negative numbers in the list (negative means less than 0).
numbers3 = [2, -1, 8, 10, -7, 6]
total = 0
for i in range(len(numbers3)):  
    item = numbers3[i]  
    if item <= 0:  
        total = total + item
print("The sum of only the positive numbers is:", total)


# Problem 4
# Find and print the sum of only the even numbers in the list. 
numbers4 = [8, 3, 15, 22, 11, 6]
total = 0
for i in range (len(numbers4)):
    item = numbers4[i]
    if item % 2 == 0:
        print("total")





# Problem 5
# Find and print the biggest number that is negative in the list.
numbers5 = [-1, -30, -5, 7, 12, -2]
biggest = -9999
for i in range(len(numbers5)):
    item = numbers5[i]
    if item > biggest and item < 0:
        biggest = item
