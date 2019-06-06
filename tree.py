import sys
import subprocess
import os

# tree.py PATH
# writes a txt file that shows the tree structure of the PATH
"""
PATH
- PATH/first_alphabetical_dir
-* PATH/first_alphabetical_dir/fileA
-- PATH/first_alphabetical_dir/inside_dir
--* PATH/fire_alphabetical_dir/inside_dir/fileB

NOTE:
    in each directory, files are listed before subdirectories
"""

args = sys.argv
path = ""

# get path from user, or use current working directory by default
if len(args) == 1:
    path = os.getcwd()
else:
    path = args[1]

print("PATH", path)
num_files = 0

# open a file to write
# format: TREE_PATH.txt
modified_path = path.replace('/', '_')
saved_file = open("TREE_{}.txt".format(modified_path), "w+")
saved_file.write("Tree at " + path + "\n\n")


# recursively write the tree to saved_file
def print_dir(path, saved_file, depth):
    """
    path: current path
    saved_file: global shared file to save to
    depth: depth of tree, indicates how many directories deep the algorithm is
    """
    
    is_dir = not os.path.isfile(path)

    if is_dir:
        current_dir = os.listdir(path)

        # get a list of all directories in 'path'
        dir_list = [x for x in current_dir if os.path.isdir(os.path.join(path, x))]

        # get a list of all files in 'path'
        file_list = [x for x in current_dir if not os.path.isdir(os.path.join(path, x))]

        for file in file_list:
            global num_files
            num_files += 1
            saved_file.write("-" * depth + "* " + os.path.basename(file)  + "\n")

        for dir in dir_list:
            # filename = os.fsdecode(file)
            saved_file.write("-" * depth + " " + dir + "/" + "\n")
            print_dir(path + "/" + dir, saved_file, depth+1)

    return


print_dir(path, saved_file, 0)

saved_file.write("\n" + "Files: " + str(num_files))
saved_file.close()