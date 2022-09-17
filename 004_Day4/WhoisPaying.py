# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
num_names = len(names)
random_person = random.randint(0, num_names-1)
print(f"Today bill is going to be paid by {names[random_person]}")
