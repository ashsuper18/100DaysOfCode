import random
from unittest import result
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

# ?# students_scores = {new_key:new_value for item in list}
# students_scores = {nom: random.randint(10, 95) for nom in names}
# print(students_scores)

# ? # new_dict = {new_key:new_vlaue for (key,value) in dict.items() if test}
# passed_students = {students: score for (students, score) in students_scores.items() if score > 50}
# print(passed_students)

# Exrcise
# # q1 Coount word length and convet it into dictinory
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# list1 = sentence.split()
# result = {key: len(key) for key in list1}
# print(result)

# Q2
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# weather_f = {day: (temp_c * (9/5)+32) for (day, temp_c) in weather_c.items()}
# print(weather_f)
