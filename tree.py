import sys
import subprocess
import os

# tree.py PATH
# writes a txt file that shows the tree structure of the PATH
"""
PATH
->PATH/first_alphabetical_dir
->PATH/first_alphabetical_dir/fileA
-->PATH/first_alphabetical_dir/inside_dir
-->...
->...

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
modified_path = path.replace('/', '_')
saved_file = open("TREE_{}.txt".format(modified_path), "w+")
saved_file.write("Tree at " + path + "\n\n")


# recursively write the tree to saved_file
def print_dir(path, saved_file):
    is_dir = not os.path.isfile(path)

    # print(path, is_dir)

    if is_dir:

        # get a list of the files in the path
        current_dir = os.listdir(path)
        for file in current_dir:
            # print(file)
            # filename = os.fsdecode(file)
            print_dir(path + "/" + file, saved_file)

        # saved_file.write(str(os.path.isfile(path + "/" + filename)) + "\n")
    else:
        global num_files
        num_files += 1
        saved_file.write(path + "\n")

    return


print_dir(path, saved_file)

saved_file.write("\n" + "Files: " + str(num_files))
saved_file.close()

