import json
import os
import shutil
import csv
from datetime import datetime

students = []
update_count = 0


def get_valid_name():
    while True:
        name = input("Enter Name: ").strip()

        if not name:
            print("Name cannot be empty!")
            continue

        if any(char.isdigit() for char in name):
            print("Name cannot contain digits!")
            continue

        return name
 
    

def get_valid_roll():
    while True:
        try:
            roll = int(input("Enter Roll Number: "))

            if roll <= 0:
                print("Roll Number must be greater than 0!")
            else:
                return roll

        except ValueError:
            print("Invalid Roll Number!")



def get_valid_age():
    while True:
        try:
            age = int(input("Enter Age: "))

            if 18 <= age <= 60:
                return age
            else:
                print("Age must be between 18 and 60!")

        except ValueError:
            print("Invalid Age!")



def get_valid_marks():
    while True:
        try:
            marks = float(input("Enter Marks: "))

            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be between 0 and 100!")

        except ValueError:
            print("Invalid Marks!")



def get_valid_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Value must be greater than 0!")
            else:
                return value
        except ValueError:
            print("Invalid Input!")



def get_valid_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid Input!")



def add_student():
    roll = get_valid_int("Enter Roll Number: ")

    # Check for duplicate roll number
    for student in students:
        if student["roll"] == roll:
            print("Error: Roll Number already exists!")
            return

    name = get_valid_name()
    age = get_valid_age()
    student_class = input("Enter Class: ")
    gender = input("Enter Gender (Male/Female): ")
    marks = get_valid_marks()

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
    roll = get_valid_int("Enter Roll Number to Update: ")

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
                student["name"] = get_valid_name()
            elif choice == "2":
                student["age"] = get_valid_age()
            elif choice == "3":
                student["class"] = input("Enter New Class: ")
            elif choice == "4":
                student["gender"] = input("Enter New Gender: ")
            elif choice == "5":
                student["marks"] = get_valid_marks()
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


def load_data():
    global students
    try:
        with open(
            "students.json",
            "r"
        ) as file:
            students = json.load(file)
        print(
            f"{len(students)} Students Loaded."
        )

    except FileNotFoundError:
        students = []
        print(
            "No Previous Data Found."
        )
    except json.JSONDecodeError:
        students = []

        print(
            "JSON File Corrupted."
        )

def save_data():
    with open('students.json', 'w') as f:
        json.dump(students, f, indent=4)

def export_backup():
    try:
        shutil.copy(
            "students.json",
            "students_backup.json"
        )

        print(
            "Backup Created Successfully."
        )
    except FileNotFoundError:
        print(
            "No Data File Found For Backup."
        )


def export_csv():

    if not students:
        print("No students found.")
        return

    with open(
        "students.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow(
            ["Roll", "Name", "Age", "Class", "Gender", "Marks"]
        )

        for student in students:

            writer.writerow([
                student["roll"],
                student["name"],
                student["age"],
                student["class"],
                student["gender"],
                student["marks"]
            ])

    print(
        "CSV Exported Successfully."
    )

def import_backup():

    global students

    try:

        with open(
            "students_backup.json",
            "r"
        ) as file:

            students = json.load(file)

        save_data()

        print(
            "Backup Restored Successfully."
        )

    except FileNotFoundError:

        print(
            "Backup File Not Found."
        )
    except json.JSONDecodeError:
        print(
            "Backup File Corrupted."
        )

def display_file_size():

    try:

        size = os.path.getsize(
            "students.json"
        )

        size_kb = size / 1024

        print(
            f"Data File Size: {size_kb:.2f} KB"
        )

    except FileNotFoundError:

        print(
            "Data File Not Found."
        )

def create_auto_backup():

    try:

        shutil.copy(
            "students.json",
            "students_backup.json"
        )

        print(
            "Automatic Backup Created."
        )

    except FileNotFoundError:

        print(
            "No Data File Found For Backup."
        )

def display_last_backup_time():
    try:

        timestamp = os.path.getmtime(
            "students_backup.json"
        )

        backup_time = datetime.fromtimestamp(
            timestamp
        )

        print(
            f"Last Backup Time: {backup_time.strftime('%Y-%m-%d %H:%M:%S')}"
        )

    except FileNotFoundError:

        print(
            "Backup File Not Found."
        )

def delete_student():
    roll = get_valid_int("Enter Roll Number to Delete: ")
    for i, student in enumerate(students):
        if student.get('roll') == roll:
            del students[i]
            save_data()
            print("Student Deleted Successfully!")
            return
    print("Student Not Found!")

def display_update_count():
    print(f"\nTotal Updates: {update_count}")


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

    roll = get_valid_int("Enter Roll Number: ")

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


def student_menu():
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Save Data")
    print("7. Display Update Count")
    print("8. Display Statistics")
    print("9. Student Report Card")
    print("10. Backup Data")
    print("11. Import Backup")
    print("12. Display File Size")
    print("13. Last Backup Time")
    print("14. Export CSV")
    print("15. Exit")



create_auto_backup()

load_data()

while True:
    student_menu()

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        save_data()

    elif choice == "7":
        display_update_count()

    elif choice == "8":
        display_statistics()

    elif choice == "9":
        student_report()

    elif choice == "10":
        export_backup()

    elif choice == "11":
        import_backup()

    elif choice == "12":
        display_file_size()

    elif choice == "13":
        display_last_backup_time()

    elif choice == "14":
        export_csv()

    elif choice == "15":
        save_data()
        print("Thank you for using the Student Management System.")
        break
    
    else:
        print("Invalid Choice!")