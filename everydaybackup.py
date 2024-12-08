import os
import shutil
import datetime

# Define source and destination paths
SOURCE_DIR = "/path/to/source_directory"  # Replace with the directory to back up
DEST_DIR = "/path/to/backup_directory"   # Replace with the backup location

# Function to create a daily backup
def backup_files():
    try:
        # Get current date for backup folder naming
        today_date = datetime.datetime.now().strftime("%Y-%m-%d")
        backup_path = os.path.join(DEST_DIR, f"backup_{today_date}")

        # Check if today's backup already exists
        if os.path.exists(backup_path):
            print(f"Backup for {today_date} already exists at {backup_path}.")
            return

        # Create a new backup folder
        os.makedirs(backup_path)

        # Copy files and directories from source to backup location
        for item in os.listdir(SOURCE_DIR):
            source_item = os.path.join(SOURCE_DIR, item)
            dest_item = os.path.join(backup_path, item)

            if os.path.isdir(source_item):
                shutil.copytree(source_item, dest_item)
                print(f"Directory backed up: {source_item}")
            else:
                shutil.copy2(source_item, dest_item)
                print(f"File backed up: {source_item}")

        print(f"Backup completed successfully! Files are saved in {backup_path}.")
    except Exception as e:
        print(f"Error during backup: {e}")

# Run the backup
if __name__ == "__main__":
    backup_files()
