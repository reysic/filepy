import sys
import os
import time

provided_path = sys.argv[1]
older_than_days = int(sys.argv[2])
print(f"Finding files in {provided_path} older than {older_than_days} days...")

SECONDS_IN_DAY = 86400
time_now = time.time()
cutoff_time = time_now - (older_than_days * SECONDS_IN_DAY)

file_paths_to_remove = []
num_files_to_keep = 0

for (dirpath, dirnames, filenames) in os.walk(provided_path):
    for f in filenames:
        file_path = os.path.join(dirpath, f)
        if os.path.getctime(file_path) < cutoff_time:
            file_paths_to_remove.append(file_path)
        else:
            num_files_to_keep += 1

user_file_remove_res = (
    input(
        f"{len(file_paths_to_remove)} files will be removed and {num_files_to_keep} will be kept. Continue? (y/N): "
    )
    .lower()
    .strip()[:1]
)
if not user_file_remove_res == "y":
    sys.exit(1)

num_files_removed = 0
for file_path in file_paths_to_remove:
    os.remove(file_path)
    num_files_removed += 1

print(f"{num_files_removed} files successfully removed ✨")

user_dir_remove_res = input(f"Remove empty directories? (y/N): ").lower().strip()[:1]
if not user_dir_remove_res == "y":
    sys.exit(1)

dir_paths_to_remove = []

for (dirpath, dirnames, filenames) in os.walk(provided_path):
    for d in dirnames:
        dir_path = os.path.join(dirpath, d)
        if not os.listdir(dir_path):
            dir_paths_to_remove.append(dir_path)

num_dirs_removed = 0
for dir_path in dir_paths_to_remove:
    os.rmdir(dir_path)
    num_dirs_removed += 1

print(f"{num_dirs_removed} empty directories successfully removed ✨")

sys.exit(0)
