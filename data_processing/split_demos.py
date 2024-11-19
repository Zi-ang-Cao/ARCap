import os
import shutil

copy_to_new_folder = True

# Path to the root folder
root_folder = "./data/2024-11-18-17-49-20_backup"

# Paths to new folders A and B
folder_a = os.path.abspath(os.path.join(root_folder, "../2024-11-18-17-49-20_assemble_level_1_pink_on_yellow"))
folder_b = os.path.abspath(os.path.join(root_folder, "../2024-11-18-17-49-20_assemble_level_1_pink_on_blue"))

# Create folders A and B if they don't exist
os.makedirs(folder_a, exist_ok=True)
os.makedirs(folder_b, exist_ok=True)

# Get a sorted list of all subfolders in the root folder
subfolders = sorted([f for f in os.listdir(root_folder) if os.path.isdir(os.path.join(root_folder, f))])
print(f"Found {len(subfolders)} subfolders in the root folder.")

# Copy the first 61 subfolders to folder A, and the rest to folder B
for i, subfolder in enumerate(subfolders):
    src = os.path.join(root_folder, subfolder)
    if i < 61:
        dst = os.path.join(folder_a, subfolder)
    else:
        dst = os.path.join(folder_b, subfolder)
    if copy_to_new_folder:
        shutil.copytree(src, dst)
    else:
        shutil.move(src, dst)

# Copy all remaining files in the root folder to both folder A and folder B
files = [f for f in os.listdir(root_folder) if os.path.isfile(os.path.join(root_folder, f))]
print(f"Found {len(files)} files in the root folder (excluding subfolders).")

for file in files:
    src_file = os.path.join(root_folder, file)
    shutil.copy(src_file, folder_a)  # Copy file to folder A
    shutil.copy(src_file, folder_b)  # Copy file to folder B

print(f"Subfolders and remaining files have been successfully organized into folders A ({folder_a}) and B ({folder_b}).")
