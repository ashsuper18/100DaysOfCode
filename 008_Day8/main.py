# def greet(name, age):
#     print(f"Hello {name} Your age is {age}")
# greet(name="Ash", age=12)

import math
# Write your code below this line 👇


def paint_calc(height, width, coverage):
    number_of_can = math.ceil((height * width) / coverage)
    print("Total cans: "+number_of_can)


# Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, coverage=coverage)
