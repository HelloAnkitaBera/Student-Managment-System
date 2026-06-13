import json

students = []


def add_student():
    roll = int(input("Enter Roll Number: "))

    # Check for duplicate roll number
    for student in students:
        if student["roll"] == roll:
            print("Error: Roll Number already exists!")
            return

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    student_class = input("Enter Class: ")
    gender = input("Enter Gender (Male/Female): ")
    marks = float(input("Enter Marks: "))

    student = {
        "roll": roll,
        "name": name,
        "age": age,
        "class": student_class,
        "gender": gender,
        "marks": marks
    }

    students.append(student)

    print("Student Added Successfully!")


def view_students():
    if not students:
        print("No students found.")
        return

    print(f"\nTotal Students: {len(students)}")

    print("-" * 80)
    print(f"{'Roll':<10}{'Name':<15}{'Age':<10}{'Class':<10}{'Gender':<15}{'Marks':<10}")
    print("-" * 80)

    for student in students:
        print(
            f"{student['roll']:<10}"
            f"{student['name']:<15}"
            f"{student['age']:<10}"
            f"{student['class']:<10}"
            f"{student.get('gender', 'N/A'):<15}"
            f"{student['marks']:<10}"
        )

    print("-" * 80)


def search_student():
    keyword = input("Enter Roll Number or Name: ")

    found = False

    print("\nSearch Results")
    print("-" * 80)
    print(f"{'Roll':<10}{'Name':<15}{'Age':<10}{'Class':<10}{'Gender':<15}{'Marks':<10}")
    print("-" * 80)

    for student in students:
        if (keyword.isdigit() and student["roll"] == int(keyword)) or \
           (keyword.lower() in student["name"].lower()):

            print(
                f"{student['roll']:<10}"
                f"{student['name']:<15}"
                f"{student['age']:<10}"
                f"{student['class']:<10}"
                f"{student.get('gender', 'N/A'):<15}"
                f"{student['marks']:<10}"
            )

            found = True

    if found:
        print("-" * 80)
    else:
        print("Student Not Found!")


def update_student():
    roll = int(input("Enter Roll Number to Update: "))

    for student in students:
        if student["roll"] == roll:

            student["name"] = input("New Name: ")
            student["age"] = int(input("New Age: "))
            student["class"] = input("New Class: ")
            student["gender"] = input("New Gender: ")
            student["marks"] = float(input("New Marks: "))

            print("Student Updated Successfully!")
            return

    print("Student Not Found!")


def delete_student():
    roll = int(input("Enter Roll Number to Delete: "))

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            print("Student Deleted Successfully!")
            return

    print("Student Not Found!")


def save_data():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

    print("Data Saved Successfully!")


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
