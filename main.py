students = []

def add_student():
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    student_class = input("Enter Class: ")
    marks = float(input("Enter Marks: "))

    student = {
        "roll": roll,
        "name": name,
        "age": age,
        "class": student_class,
        "marks": marks
    }

    students.append(student)

    print("Student Added Successfully!")

def view_students():
    if not students:
        print("No students found.")
        return

    for student in students:
        print(student)

def search_student():
    roll = int(input("Enter Roll Number: "))

    for student in students:
        if student["roll"] == roll:
            print(student)
            return

    print("Student Not Found!")

def update_student():
    roll = int(input("Enter Roll Number: "))

    for student in students:
        if student["roll"] == roll:

            student["name"] = input("New Name: ")
            student["age"] = int(input("New Age: "))
            student["class"] = input("New Class: ")
            student["marks"] = float(input("New Marks: "))

            print("Updated Successfully!")
            return

    print("Student Not Found!")

def delete_student():
    roll = int(input("Enter Roll Number: "))

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            print("Student Deleted Successfully!")
            return

    print("Student Not Found!")

import json

def save_data():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

    print("Data Saved Successfully!")

import json

def load_data():
    global students

    try:
        with open("students.json", "r") as file:
            students = json.load(file)

    except FileNotFoundError:
        students = []

def menu():
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Save Data")
    print("7. Exit")

students = []

load_data()

while True:

    menu()

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
        save_data()
        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")