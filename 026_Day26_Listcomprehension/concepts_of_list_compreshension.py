# TOPIC:  List compreshension
# ? NOTES: #%% to open cells and use interective window(in vs code)

# list comprehension
# #? CONCEPT: new_list  = [new_item for item in lists]
# numbers = [1, 2, 3]
# new_num = [n+1 for n in numbers]
# print(new_num)

# range_list = range(1, 5)
# new_num = [n*2 for n in range_list]
# print(new_num)

# conditional list comprehension
# # ? CONCEPT: new_list  = [new_item for item in lists if test]
# lists = [1, 2, 3, 4, 5, 6]
# new_list = [n*3 for n in lists if n > 3]
# print(new_list)


# # Example
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# short_name = [name[0:3] for name in names if len(name) > 3]
# print(short_name)

# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# short_name = [name.upper() for name in names if len(name)>4]
# print(short_name)

# # Q1
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# sq_numbers = [n*n for n in numbers]
# print(sq_numbers)

# # Q2
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# even_list = [n for n in numbers if n % 2 == 0]
# # even_list = [num % 2 == 0 for num in numbers]
# print(even_list)
