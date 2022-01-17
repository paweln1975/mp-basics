import os
import fnmatch

root = "/home/centos/IdeaProjects/mp-basics"

for path, directories, files in os.walk(root, topdown=True):
    if path.find(".git") == -1:
        if len(fnmatch.filter(files, "*.py")) > 0:
            print(path)
        for f in fnmatch.filter(files, "*.py"):
            access_r = os.access(path + "/" + f, os.R_OK)
            access_w = os.access(path + "/" + f, os.W_OK)
            access_x = os.access(path + "/" + f, os.X_OK)
            print(f"\t{f} r:{access_r} w:{access_w} x:{access_x}")


def python_files(directory):
    for path1, _, files1 in os.walk(directory, topdown=True):
        for file_path in fnmatch.filter(files1, "*.py"):
            absolute_path = os.path.abspath(path1)
            yield os.path.join(absolute_path, file_path)


print("=" * 80)

files = python_files(root)
for f in files:
    print(f)
