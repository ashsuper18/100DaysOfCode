import pandas as pd
student_dict = {
    "student": ["Ashish", "James", "lily"],
    "score": [15, 12, 18]
}
# # Basic way to loop through dictanory
# for (key,value) in student_dict.items():
#     print(key)


student_data_frame = pd.DataFrame(student_dict)
# print(student_data_frame)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # print(row)
    print(row.student)
