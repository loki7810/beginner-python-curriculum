colors = ["red", "orange", "yellow", "green", "blue","purple"] # index starts with 0
print(colors)
print(colors[3])#accessed items in a list by index
print("fourth color:", colors[3])

# print( colors[10]) # Err: out of range 

colors.append("black")
print(colors)
colors.insert(2, "brown")
print(colors)

colors.remove("green") # Removes the first occurence of item

print(colors)
index_of_blue = colors.index("blue")
print("Index of 'blue':", index_of_blue)

colors.append("blue")
blue_count = colors.count("black")
print("Count of blue:" , blue_count)

colors.sort()
print(colors)

colors.reverse() # flips order #
print(colors)



