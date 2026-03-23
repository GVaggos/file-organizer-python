import os
import shutil
import sys

EXTENSIONS = {
    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".mp4": "Videos",
    ".zip": "Archives",
    ".exe": "Programs",
}

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("Path not found.")
        return

    print(f"Organizing files in: {folder_path}")
    moved_files = 0

    for file_name in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file_name)

        if os.path.isfile(full_path):
            _, extension = os.path.splitext(file_name)
            extension = extension.lower()

            folder_name = EXTENSIONS.get(extension, "Others")
            target_folder = os.path.join(folder_path, folder_name)

            os.makedirs(target_folder, exist_ok=True)

            try:
                shutil.move(full_path, os.path.join(target_folder, file_name))
                moved_files += 1
            except Exception as e:
                print(f"Error moving {file_name}: {e}")

    print(f"Done! {moved_files} files moved.")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = input("Enter folder path: ").strip()

    organize_files(path)