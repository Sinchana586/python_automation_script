import os
from datetime import datetime

LOG_FILE = "operations_log.txt"

def write_log(message):
    with open(LOG_FILE, "a") as log:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"[{timestamp}] {message}\n")

def clean_and_rename(folder_path):
    try:
        folder_path = folder_path.strip()

        if not os.path.isdir(folder_path):
            raise FileNotFoundError(f"Folder not found: {folder_path}")

        files = os.listdir(folder_path)
        file_number = 1

        for file_name in files:
            old_path = os.path.join(folder_path, file_name)

            if not os.path.isfile(old_path):
                continue

            # Delete empty files
            if os.path.getsize(old_path) == 0:
                os.remove(old_path)
                print(f"Deleted: {file_name}")
                write_log(f"Deleted empty file: {file_name}")
                continue

            extension = os.path.splitext(file_name)[1]

            new_name = f"File_{file_number}{extension}"
            new_path = os.path.join(folder_path, new_name)

            while os.path.exists(new_path):
                file_number += 1
                new_name = f"File_{file_number}{extension}"
                new_path = os.path.join(folder_path, new_name)

            os.rename(old_path, new_path)

            print(f"Renamed: {file_name} -> {new_name}")
            write_log(f"Renamed: {file_name} -> {new_name}")

            file_number += 1

        print("\nAutomation completed successfully.")
        write_log("Automation completed successfully.")

    except FileNotFoundError as e:
        print("ERROR:", e)
        write_log(f"ERROR: {e}")

    except PermissionError:
        print("ERROR: Permission denied.")
        write_log("ERROR: Permission denied.")

    except Exception as e:
        print("Unexpected Error:", e)
        write_log(f"Unexpected Error: {e}")

# User Input
folder = input("Enter folder path: ")
clean_and_rename(folder)