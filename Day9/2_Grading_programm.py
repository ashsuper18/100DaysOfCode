student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆
student_grades = {}
for student in student_scores:
    marks = student_scores[student]
    # print(marks)
    if marks <= 70:
        student_grades[student] = "Fail"
    elif marks > 71 and marks <= 80:
        student_grades[student] = "Accetable"
    elif marks > 81 and marks <= 90:
        student_grades[student] = "Exceeds Accetable"
    else:
        student_grades[student] = "Outstanding"

print(student_grades)
