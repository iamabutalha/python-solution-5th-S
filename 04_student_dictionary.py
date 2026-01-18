# Write a program that uses a dictionary to store stident names and marks, Print the name of student with higest marks

students = {
    "sara": {"marks": [23,2,33,3]},
    "sahil": {"marks": [11,22,22,22, 22]}
}
highest_marks = None
highest_marks_name = None
i = 0

studnet_scores = {name: sum(info['marks']) for name, info in students.items()}
print(studnet_scores)

top_student = max(studnet_scores, key=studnet_scores.get)
top_marks = studnet_scores[top_student]

print(top_student)

# student_with_higest = max(students, key=students.get("marks"))

# print(highest_marks, highest_marks_name)