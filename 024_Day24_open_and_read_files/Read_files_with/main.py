file = open("024_Day24_open_and_read_files\Read_files_with\my_data.txt")
# file = open("./my_data.txt")
contents = file.read()
print(contents)
file.close()


# # ! or we can use with to open and  close it automatically
# # ? reading the file
# with open("024_Day24_open_and_read_files\Read_files_with\my_data.txt") as file:
#     contents = file.read()
#     print(contents)

# # now writing the file
# # ? mode = "w" is write and mode="a" is append
# with open("024_Day24_open_and_read_files\Read_files_with\my_data.txt", mode="a") as file:
#     file.write("\nNew text.")
