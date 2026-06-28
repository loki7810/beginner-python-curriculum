nums = [5, -8, 58, -87, 7, -67, 3, 4, 6, -98]
print(nums)
total = sum(nums) # shortcut to find item
print("the sum is", total) 
print("our algorithm")

total = 0
for i in range(len(nums)): # Go through each number
        item = nums[i] # Acessing the number at index 1
        total = total + item
print("The sum is:", total )   

# find sum in pos num
total = 0
for i in range(len(nums)): # Go through each index
    item = nums[i]  # Accessing the number at index i
    total = total + item  # Add the item to the running total
print("The sum is:", total)

# Find sum of only positive numbers
total = 0
for i in range(len(nums)):  # Go through each index
    item = nums[i]  # Accessing the number at index i
    if item >= 0:  # Positive means >= 0
        total = total + item
print("The sum of only the positive numbers is:", total)






