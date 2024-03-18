import shutil
from pathlib import Path

def organize_files(source_folder, destination_folder):
    # Create destination folder if it doesn't exist
    destination_path = Path(destination_folder)
    destination_path.mkdir(parents=True, exist_ok=True)
    
    # Get list of files in source folder
    files = Path(source_folder).glob("*")
    
    # Organize files by extension
    for file_path in files:
        if file_path.is_file():
            ext = file_path.suffix.lower()
            ext_folder = destination_path / ext[1:]
            ext_folder.mkdir(parents=True, exist_ok=True)
            file_path.rename(ext_folder / file_path.name)

# Example usage
source_folder = "source_folder"
destination_folder = "organized_files"
organize_files(source_folder, destination_folder)
print("Files organized successfully!")
