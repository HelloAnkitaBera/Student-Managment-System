
import os
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def print_line(length=80):
    print("-" * length)
def print_header(title):
    print("\n" + "=" * 80)
    print(title.center(80))
    print("=" * 80)


def press_enter():
    input("\nPress Enter to continue...")


def display_menu():
    print_header("STUDENT MANAGEMENT SYSTEM")

    print("1.  Add Student")
    print("2.  View Students")
    print("3.  Search Student")
    print("4.  Update Student")
    print("5.  Delete Student")
    print("6.  Save Data")
    print("7.  Display Update Count")
    print("8.  Display Statistics")
    print("9.  Student Report Card")
    print("10. Backup Data")
    print("11. Import Backup")
    print("12. Display File Size")
    print("13. Last Backup Time")
    print("14. Export CSV")
    print("15. Storage Information")
    print("16. Exit")

    print_line()


def invalid_choice():
    print("\nInvalid Choice! Please try again.")


def success_message(message):
   print(f"\n✅ {message}")


def error_message(message):
    print(f"\n❌ {message}")