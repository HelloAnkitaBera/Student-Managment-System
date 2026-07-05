import json
import os
import shutil
import csv
from datetime import datetime

students = []


def load_data():
    global students
    try:
        with open("students.json", "r") as file:
            data = json.load(file)
            students.clear()
            students.extend(data)
        print(f"{len(students)} Students Loaded.")
    except FileNotFoundError:
        students.clear()
        print("No Previous Data Found.")
    except json.JSONDecodeError:
        students.clear()
        print("JSON File Corrupted.")


def save_data():
    with open('students.json', 'w') as f:
        json.dump(students, f, indent=4)


def export_backup():
    try:
        shutil.copy("students.json", "students_backup.json")
        print("Backup Created Successfully.")
    except FileNotFoundError:
        print("No Data File Found For Backup.")


def export_csv():
    if not students:
        print("No students found.")
        return

    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Roll", "Name", "Age", "Class", "Gender", "Marks"])
        for student in students:
            writer.writerow([
                student["roll"],
                student["name"],
                student["age"],
                student["class"],
                student["gender"],
                student["marks"]
            ])
    print("CSV Exported Successfully.")


def import_backup():
    global students
    try:
        with open("students_backup.json", "r") as file:
            data = json.load(file)
            students.clear()
            students.extend(data)
        save_data()
        print("Backup Restored Successfully.")
    except FileNotFoundError:
        print("Backup File Not Found.")
    except json.JSONDecodeError:
        print("Backup File Corrupted.")


def display_file_size():
    try:
        size = os.path.getsize("students.json")
        size_kb = size / 1024
        print(f"Data File Size: {size_kb:.2f} KB")
    except FileNotFoundError:
        print("Data File Not Found.")


def create_auto_backup():
    try:
        shutil.copy("students.json", "students_backup.json")
        print("Automatic Backup Created.")
    except FileNotFoundError:
        print("No Data File Found For Backup.")


def display_last_backup_time():
    try:
        timestamp = os.path.getmtime("students_backup.json")
        backup_time = datetime.fromtimestamp(timestamp)
        print(f"Last Backup Time: {backup_time.strftime('%Y-%m-%d %H:%M:%S')}")
    except FileNotFoundError:
        print("Backup File Not Found.")


if __name__ == "__main__":
    import os
    import subprocess
    import sys
    current_dir = os.path.dirname(os.path.abspath(__file__))
    main_path = os.path.join(current_dir, "main.py")
    subprocess.run([sys.executable, main_path])

