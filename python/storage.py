
import json
import os
import shutil
import csv

students = []
update_count = 0

DATA_FOLDER = "data"

STUDENT_FILE = os.path.join(DATA_FOLDER, "students.json")
BACKUP_FILE = os.path.join(DATA_FOLDER, "students_backup.json")
CSV_FILE = os.path.join(DATA_FOLDER, "students.csv")

def create_data_folder():


    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

def save_data():

    create_data_folder()

    with open(STUDENT_FILE, "w") as file:
        json.dump(students, file, indent=4)

    print("Data Saved Successfully.")


def load_data():
    global students

    create_data_folder()
    try:
        with open(STUDENT_FILE, "r") as file:

            students.clear()
            students.extend(json.load(file))

        print(f"{len(students)} Students Loaded.")

    except FileNotFoundError:

        students.clear()
        print("No Previous Data Found.")

    except json.JSONDecodeError:

        students.clear()
        print("JSON File Corrupted.")


def export_backup():
    create_data_folder()

    try:

        shutil.copy(STUDENT_FILE, BACKUP_FILE)

        print("Backup Created Successfully.")

    except FileNotFoundError:

        print("No Data File Found For Backup.")

def import_backup():

    global students

    create_data_folder()

    try:

        with open(BACKUP_FILE, "r") as file:

            students.clear()
            students.extend(json.load(file))

        save_data()

        print("Backup Restored Successfully.")

    except FileNotFoundError:

        print("Backup File Not Found.")

    except json.JSONDecodeError:

        print("Backup File Corrupted.")


def create_auto_backup():

    create_data_folder()

    try:

        shutil.copy(STUDENT_FILE, BACKUP_FILE)

        print("Automatic Backup Created.")

    except FileNotFoundError:

        print("No Data File Found For Backup.")


def export_csv():

    create_data_folder()

    if not students:
        print("No students found.")
        return

    with open(CSV_FILE, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(
            [
                "Roll",
                "Name",
                "Age",
                "Class",
                "Gender",
                "Marks",
                "Created At"
            ]
        )

        for student in students:

            writer.writerow([
                student["roll"],
                student["name"],
                student["age"],
                student["class"],
                student["gender"],
                student["marks"],
                student.get("created_at", "")
            ])

    print("CSV Exported Successfully.")

def display_file_size():
    try:

        size = os.path.getsize(STUDENT_FILE)

        print(f"Data File Size : {size / 1024:.2f} KB")

    except FileNotFoundError:

        print("Data File Not Found.")


def display_last_backup_time():

    from datetime import datetime

    try:

        timestamp = os.path.getmtime(BACKUP_FILE)

        backup_time = datetime.fromtimestamp(timestamp)

        print(
            f"Last Backup Time : "
            f"{backup_time.strftime('%Y-%m-%d %H:%M:%S')}"
        )

    except FileNotFoundError:

        print("Backup File Not Found.")

def increment_update_count():

    global update_count
    update_count += 1


def get_update_count():

    return update_count