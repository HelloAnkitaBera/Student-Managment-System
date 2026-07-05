from storage import *
from student import *
from reports import *

create_auto_backup()
load_data()


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
        print("Data Saved Successfully!")


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