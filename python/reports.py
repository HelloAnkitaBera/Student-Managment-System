
import os
import sys
from datetime import datetime


sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


students_module = None

try:
    import storage as students_module  
except Exception:

    try:
        from . import storage as students_module 
    except Exception:

        try:
            import importlib.util
            storage_path = os.path.join(os.path.dirname(__file__), "storage.py")
            if os.path.exists(storage_path):
                spec = importlib.util.spec_from_file_location("storage", storage_path)
                if spec is None or getattr(spec, 'loader', None) is None:
                    raise ImportError("Could not load spec or loader for storage module")
                storage = importlib.util.module_from_spec(spec)
                loader = getattr(spec, 'loader', None)
                if loader is not None and hasattr(loader, 'exec_module') and callable(getattr(loader, 'exec_module', None)):
                    loader.exec_module(storage)
                elif loader is not None and hasattr(loader, 'load_module') and callable(getattr(loader, 'load_module', None)):
                    
                    loader.load_module(spec.name)
                else:
                    raise ImportError("Storage module loader does not support exec_module or load_module")
                students_module = storage
            else:
                raise FileNotFoundError
        except Exception:
            class _EmptyStorage:
                students = []
                @staticmethod
                def display_file_size():
                    print("File size information is unavailable.")
                @staticmethod
                def display_last_backup_time():
                    print("Last backup time information is unavailable.")
                @staticmethod
                def get_update_count():
                    return 0

            students_module = _EmptyStorage()

students = getattr(students_module, "students", [])
display_file_size = getattr(
    students_module,
    "display_file_size",
    lambda: print("File size information is unavailable.")
)
display_last_backup_time = getattr(
    students_module,
    "display_last_backup_time",
    lambda: print("Last backup time information is unavailable.")
)

def get_update_count():
    return getattr(students_module, "get_update_count", lambda: 0)()

from validation import get_valid_int

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
        print("\nNo students found.")
        return

    marks_list = [student["marks"] for student in students]

    total_students = len(students)
    highest_marks = max(marks_list)
    lowest_marks = min(marks_list)
    average_marks = sum(marks_list) / total_students

    print("\n========== STUDENT STATISTICS ==========")
    print(f"Total Students : {total_students}")
    print(f"Highest Marks  : {highest_marks}")
    print(f"Lowest Marks   : {lowest_marks}")
    print(f"Average Marks  : {average_marks:.2f}")
    print("========================================")


def student_report():

    roll = get_valid_int("Enter Roll Number: ")

    for student in students:

        if student["roll"] == roll:

            grade = calculate_grade(student["marks"])

            print("\n===================================")
            print("        STUDENT REPORT CARD")
            print("===================================")
            print(f"Roll Number : {student['roll']}")
            print(f"Name        : {student['name']}")
            print(f"Age         : {student['age']}")
            print(f"Class       : {student['class']}")
            print(f"Gender      : {student['gender']}")
            print(f"Marks       : {student['marks']}")
            print(f"Grade       : {grade}")
            print(f"Created At  : {student.get('created_at', 'N/A')}")
            print("===================================")

            return

    print("Student Not Found!")


def display_update_count():

    print(f"\nTotal Updates : {get_update_count()}")

def display_topper():

    if not students:
        print("No students found.")
        return

    topper = max(students, key=lambda student: student["marks"])

    print("\n========== TOPPER ==========")
    print(f"Roll Number : {topper['roll']}")
    print(f"Name        : {topper['name']}")
    print(f"Marks       : {topper['marks']}")
    print(f"Grade       : {calculate_grade(topper['marks'])}")
    print("============================")

def display_failed_students():

    failed_students = [
        student for student in students
        if student["marks"] < 40
    ]

    if not failed_students:
        print("\nNo failed students.")
        return

    print("\n========== FAILED STUDENTS ==========")

    for student in failed_students:

        print(
            f"{student['roll']:<10}"
            f"{student['name']:<20}"
            f"{student['marks']}"
        )

    print("=====================================")


def show_storage_info():

    print("\n========== STORAGE INFORMATION ==========")

    display_file_size()

    display_last_backup_time()

    print(f"Total Records : {len(students)}")

    print("=========================================")