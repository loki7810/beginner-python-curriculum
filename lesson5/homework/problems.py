# Problem 1
# Create a list of 3 operating systems.
# Print the last one using len().
# Then reverse the list and print it.
os = ["Windows", "Apple", "Chrome"]
os_len = len(os) -1
print(os[os_len])
os.reverse()
print(os)




# Problem 2
# Create a list of 4 school subjects.
# Print the second subject.
# Then sort them alphabetically and print the result.
subject = ["Social studies", "Math", "PE", "English" ]
print(subject[2])
subject.sort()
print(subject)



# Problem 3 
# Create a list of 5 error codes.
# Print how many there are.
# Then find the index of "403" and print it.
err = [404, 403, 401, 502, 301]
length = len(err)
print("Number of errors:", length)
index_of_403 = err.index(403)
print("Index of '403':", index_of_403)


# Problem 4 
# Create a list of 2 programming languages.
# Print a random one.
# Then append another language and print the list.
import random

pl = ["python", "c"]
random_pl = random.choice(pl)
print(random_pl)


# Problem 5
# Create a list of 6 passwords.
# Print the one in the middle using len().
# Then remove the first password in the list and print it.
passwwords = ["Iamsmart", "himynameismarcus", "K9#mP7$qL2@vN8*jR5", "qwerty54765**", "Iampoor2348967", "erghieru123$$$"]





    