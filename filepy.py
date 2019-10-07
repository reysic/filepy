import sys
import os

provided_path = sys.argv[1]
print("Provided path:", provided_path)

dir_iterator = os.scandir(provided_path)
file_paths = [f.path for f in os.scandir(provided_path) if f.is_file()]
dir_paths = [f.path for f in dir_iterator if f.is_dir()]

print("\nFiles:")
print(len(file_paths))
print(*file_paths, sep="\n")

print("\nFolders:")
print(len(dir_paths))
print(*dir_paths, sep="\n")
