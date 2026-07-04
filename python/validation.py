# validation.py


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

            print("Age must be between 18 and 60!")

        except ValueError:
            print("Invalid Age!")


def get_valid_marks():
    

    while True:
        try:
            marks = float(input("Enter Marks: "))

            if 0 <= marks <= 100:
                return marks

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


def get_valid_gender():
    while True:
        gender = input("Enter Gender (Male/Female): ").strip().capitalize()

        if gender in ["Male", "Female"]:
            return gender

        print("Invalid Gender! Enter Male or Female.")


def get_valid_class():
    while True:
        student_class = input("Enter Class: ").strip()

        if student_class:
            return student_class

        print("Class cannot be empty!")