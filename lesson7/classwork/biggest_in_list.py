nums = [7,  1, -4, 6, -9, -1, -5]
 #you can use built in py functions to find
biggestitem = max(nums)
smallestitem = min(nums)
print("the biggest item is", biggestitem)
print("the biggest item is", smallestitem)
print("our al")
b = nums[0] # starts by assuming 1st as biggest
for i in range(len(nums)):
    if nums[i] > b:
       biggest = nums[i]
print("the biggest item is", b)

