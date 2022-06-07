student_scores = {
    "Harry" : 85,
    "Ron" : 15,
    "Hermione" : 69,
    "Morty" : 99,
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "You can be partners with Rick Sanchez."
    elif score > 80:
        student_grades[student] = "J.K. Rowling will love you."
    elif score > 60:
        student_grades[student] = "Be with Rahil😏"
    else:
        student_grades[student] = "FAIL. Why do you exist?🤨"

print(student_grades)
