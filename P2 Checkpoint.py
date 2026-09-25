print("=== STUDENT GRADE CHECKER ===")

students = int(input("Enter number of students: "))

while students < 3:
    print("You need to enter 3 or more students.")
    students = int(input("Enter number of students: "))

for student in range(1, students + 1):
    print("\nStudent #", student)

    student_name = input("Name: ")

    score1 = float(input("Enter score for Activity 1: "))
    score2 = float(input("Enter score for Activity 2: "))
    score3 = float(input("Enter score for Activity 3: "))

    total = score1 + score2 + score3
    grade = total / 3

    if grade >= 90:
        result = "Excellent"
    elif grade >= 80:
        result = "Very Good"
    elif grade >= 75:
        result = "Passed"
    else:
        result = "Failed"

    print("\n--- Student Result ---")
    print("Student:", student_name)
    print("Average Grade:", round(grade, 2))
    print("Result:", result)
