# student.py

from datetime import datetime

from validation import (
    get_valid_name,
    get_valid_age,
    get_valid_marks,
    get_valid_int,
    get_valid_gender,
    get_valid_class
)

import json
import os
import storage

students = storage.students



def add_student():
    """Add a new student."""

    roll = get_valid_int("Enter Roll Number: ")

    # Check duplicate roll number
    for student in students:
        if student["roll"] == roll:
            print("Error: Roll Number already exists!")
            return

    name = get_valid_name()
    age = get_valid_age()
    student_class = get_valid_class()
    gender = get_valid_gender()
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
    storage.save_data()

    print("Student Added Successfully!")


def view_students():
    """Display all students."""

    if not students:
        print("No students found.")
        return

    print(f"\nTotal Students : {len(students)}")

    print("-" * 110)
    print(
        f"{'Roll':<10}"
        f"{'Name':<20}"
        f"{'Age':<8}"
        f"{'Class':<10}"
        f"{'Gender':<12}"
        f"{'Marks':<10}"
        f"{'Created At':<25}"
    )
    print("-" * 110)

    for student in students:
        print(
            f"{student['roll']:<10}"
            f"{student['name']:<20}"
            f"{student['age']:<8}"
            f"{student['class']:<10}"
            f"{student['gender']:<12}"
            f"{student['marks']:<10}"
            f"{student['created_at']:<25}"
        )

    print("-" * 110)


def search_student():


    keyword = input("Enter Name/Roll Number: ").strip()

    found = False

    for student in students:

        if (
            keyword.isdigit()
            and student["roll"] == int(keyword)
        ) or (
            keyword.lower() in student["name"].lower()
        ):

            if not found:

                print("\nStudent Found")
                print("-" * 80)
                print(
                    f"{'Roll':<10}"
                    f"{'Name':<20}"
                    f"{'Age':<8}"
                    f"{'Class':<10}"
                    f"{'Gender':<12}"
                    f"{'Marks':<10}"
                )
                print("-" * 80)

            print(
                f"{student['roll']:<10}"
                f"{student['name']:<20}"
                f"{student['age']:<8}"
                f"{student['class']:<10}"
                f"{student['gender']:<12}"
                f"{student['marks']:<10}"
            )

            found = True

    if found:
        print("-" * 80)
    else:
        print("Student Not Found!")


def update_student():


    roll = get_valid_int("Enter Roll Number to Update: ")

    for student in students:

        if student["roll"] == roll:

            print("\nCurrent Student Details")
            print("-" * 80)

            print(
                f"{'Roll':<10}"
                f"{'Name':<20}"
                f"{'Age':<8}"
                f"{'Class':<10}"
                f"{'Gender':<12}"
                f"{'Marks':<10}"
            )

            print("-" * 80)

            print(
                f"{student['roll']:<10}"
                f"{student['name']:<20}"
                f"{student['age']:<8}"
                f"{student['class']:<10}"
                f"{student['gender']:<12}"
                f"{student['marks']:<10}"
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
                student["class"] = get_valid_class()

            elif choice == "4":
                student["gender"] = get_valid_gender()

            elif choice == "5":
                student["marks"] = get_valid_marks()

            else:
                print("Invalid Choice!")
                return

            confirm = input("Save Changes? (Y/N): ").upper()

            if confirm == "Y":

                storage.increment_update_count()

                storage.save_data()

                print("Student Updated Successfully!")

            else:
                print("Update Cancelled!")

            return

    print("Student Not Found!")


def delete_student():
    """Delete a student."""

    roll = get_valid_int("Enter Roll Number to Delete: ")

    for index, student in enumerate(students):

        if student["roll"] == roll:

            print("\nStudent Found")
            print(f"Roll   : {student['roll']}")
            print(f"Name   : {student['name']}")
            print(f"Class  : {student['class']}")
            print(f"Marks  : {student['marks']}")

            confirm = input("\nAre you sure? (Y/N): ").upper()

            if confirm == "Y":

                del students[index]

                storage.save_data()

                print("Student Deleted Successfully!")

            else:

                print("Deletion Cancelled!")

            return

    print("Student Not Found!")


def student_exists(roll):


    for student in students:
        if student["roll"] == roll:
            return True

    return False