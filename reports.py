import validation
from storage import students


def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "D"


def display_statistics():
    if not students:
        print("No students found.")
        return

    marks_list = [student["marks"] for student in students]

    total_students = len(students)
    highest_marks = max(marks_list)
    lowest_marks = min(marks_list)
    average_marks = sum(marks_list) / total_students

    print("\n===== STUDENT STATISTICS =====")
    print(f"Total Students : {total_students}")
    print(f"Highest Marks  : {highest_marks}")
    print(f"Lowest Marks   : {lowest_marks}")
    print(f"Average Marks  : {average_marks:.2f}")


def student_report():
    roll = validation.get_valid_int("Enter Roll Number: ")

    for student in students:
        if student["roll"] == roll:
            grade = calculate_grade(student["marks"])

            print("\n--------------------------------")
            print("Student Report")
            print("--------------------------------")
            print(f"Roll Number : {student['roll']}")
            print(f"Name        : {student['name']}")
            print(f"Class       : {student['class']}")
            print(f"Marks       : {student['marks']}")
            print(f"Gender      : {student['gender']}")
            print(f"Grade       : {grade}")
            print("--------------------------------")
            return

    print("Student Not Found!")


if __name__ == "__main__":
    import os
    import subprocess
    import sys
    current_dir = os.path.dirname(os.path.abspath(__file__))
    main_path = os.path.join(current_dir, "main.py")
    subprocess.run([sys.executable, main_path])

