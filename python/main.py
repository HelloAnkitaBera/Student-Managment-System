# main.py
import utils

print(utils.__file__)
print(dir(utils))
import python.storage as storage
import importlib

# Import storage module once and resolve optional symbols with safe fallbacks.
storage = importlib.import_module('storage')

load_data = getattr(storage, 'load_data')
save_data = getattr(storage, 'save_data')

import_backup = getattr(storage, 'import_backup', lambda: print("Import backup not available in this storage implementation."))
export_backup = getattr(storage, 'export_backup', lambda: print("Export backup not available in this storage implementation."))
create_auto_backup = getattr(storage, 'create_auto_backup', lambda: None)
display_file_size = getattr(storage, 'display_file_size', lambda: print("Display file size not available in this storage implementation."))
display_last_backup_time = getattr(storage, 'display_last_backup_time', lambda: print("Display last backup time not available in this storage implementation."))
export_csv = getattr(storage, 'export_csv', lambda: print("Export CSV not available in this storage implementation."))

from reports import (
    display_statistics,
    student_report,
    display_update_count,
    show_storage_info
)

from utils import (
    display_menu,
    invalid_choice
)


def main():
    create_auto_backup()
    load_data()

    while True:

        display_menu()

        choice = input("Enter Choice: ").strip()

        if choice == "1":
            getattr(storage, 'add_student', lambda: print("Add student not available."))()

        elif choice == "2":
            getattr(storage, 'view_students', lambda: print("View students not available."))()

        elif choice == "3":
            getattr(storage, 'search_student', lambda: print("Search student not available."))()

        elif choice == "4":
            getattr(storage, 'update_student', lambda: print("Update student not available."))()

        elif choice == "5":
            getattr(storage, 'delete_student', lambda: print("Delete student not available."))()

        elif choice == "6":
            save_data()

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
            show_storage_info()

        elif choice == "16":
            save_data()
            print("\nThank you for using the Student Management System.")
            break

        else:
            invalid_choice()


if __name__ == "__main__":
    main()