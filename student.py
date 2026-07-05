from datetime import datetime
import validation
from storage import students, save_data

update_count = 0


def display_update_count():
    print(f"\nTotal Updates: {update_count}")


def add_student():
    roll = validation.get_valid_int("Enter Roll Number: ")

    # Check for duplicate roll number
    for student in students:
        if student["roll"] == roll:
            print("Error: Roll Number already exists!")
            return

    name = validation.get_valid_name()
    age = validation.get_valid_age()
    student_class = input("Enter Class: ")
    gender = input("Enter Gender (Male/Female): ")
    marks = validation.get_valid_marks()

    student = {
        "roll": roll,
        "name": name,
        "age": age,
        "class": student_class,
        "gender": gender,
        "marks": marks,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    students.append(student)
    save_data()
    print("Student Added Successfully!")


def view_students():
    if not students:
        print("No students found.")
        return

    print(f"\nTotal Students: {len(students)}")

    print("-" * 110)
    print(f"{'Roll':<10}{'Name':<15}{'Age':<10}{'Class':<10}{'Gender':<15}{'Marks':<10}{'Created At':<30}")
    print("-" * 110)

    for student in students:
        print(
            f"{student.get('roll', 'N/A'):<10}"
            f"{student.get('name', 'N/A'):<15}"
            f"{student.get('age', 'N/A'):<10}"
            f"{student.get('class', 'N/A'):<10}"
            f"{student.get('gender', 'N/A'):<15}"
            f"{student.get('marks', 'N/A'):<10}"
            f"{student.get('created_at', 'N/A'):<30}"
        )

    print("-" * 80)


def search_student():
    keyword = input("Enter Name/Roll No: ")

    found = False

    for student in students:
        if (keyword.isdigit() and student["roll"] == int(keyword)) or \
           (keyword.lower() in student["name"].lower()):

            if not found:
                print("\nStudent Found")
                print("-" * 80)
                print(f"{'Roll':<10}{'Name':<15}{'Age':<10}{'Class':<10}{'Gender':<15}{'Marks':<10}")
                print("-" * 80)

            print(
                f"{student.get('roll', 'N/A'):<10}"
                f"{student.get('name', 'N/A'):<15}"
                f"{student.get('age', 'N/A'):<10}"
                f"{student.get('class', 'N/A'):<10}"
                f"{student.get('gender', 'N/A'):<15}"
                f"{student.get('marks', 'N/A'):<10}"
            )

            found = True

    if found:
        print("-" * 80)
    else:
        print("Student Not Found!")


def update_student():
    global update_count
    roll = validation.get_valid_int("Enter Roll Number to Update: ")

    for student in students:
        if student["roll"] == roll:

            print("\nCurrent Student Details")
            print("-" * 80)
            print(f"{'Roll':<10}{'Name':<15}{'Age':<10}{'Class':<10}{'Gender':<15}{'Marks':<10}")
            print("-" * 80)

            print(
                f"{student.get('roll', 'N/A'):<10}"
                f"{student.get('name', 'N/A'):<15}"
                f"{student.get('age', 'N/A'):<10}"
                f"{student.get('class', 'N/A'):<10}"
                f"{student.get('gender', 'N/A'):<15}"
                f"{student.get('marks', 'N/A'):<10}"
            )

            print("-" * 80)

            print("\nWhat do you want to update?")
            print("1. Name")
            print("2. Age")
            print("3. Class")
            print("4. Gender")
            print("5. Marks")

            choice = input("Enter Choice: ")

            if choice == "1":
                student["name"] = validation.get_valid_name()
            elif choice == "2":
                student["age"] = validation.get_valid_age()
            elif choice == "3":
                student["class"] = input("Enter New Class: ")
            elif choice == "4":
                student["gender"] = input("Enter New Gender: ")
            elif choice == "5":
                student["marks"] = validation.get_valid_marks()
            else:
                print("Invalid Choice!")
                return

            confirm = input("Save Changes? (Y/N): ").upper()

            if confirm == "Y":
                update_count += 1
                save_data()
                print("Student Updated Successfully!")
                return
            else:
                print("Update Cancelled!")
                return

    print("Student Not Found!")
    return


def delete_student():
    roll = validation.get_valid_int("Enter Roll Number to Delete: ")
    for i, student in enumerate(students):
        if student.get('roll') == roll:
            del students[i]
            save_data()
            print("Student Deleted Successfully!")
            return
    print("Student Not Found!")


if __name__ == "__main__":
    import os
    import subprocess
    import sys
    current_dir = os.path.dirname(os.path.abspath(__file__))
    main_path = os.path.join(current_dir, "main.py")
    subprocess.run([sys.executable, main_path])

