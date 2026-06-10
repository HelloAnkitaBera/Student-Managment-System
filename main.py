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