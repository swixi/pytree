import sys
import subprocess
import os

#tree.py PATH
#writes a txt file that shows the tree structure of the PATH
"""
PATH
->PATH/first_alphabetical_dir
->PATH/first_alphabetical_dir/fileA
-->PATH/first_alphabetical_dir/inside_dir
-->...
->...

"""


args = sys.argv
#print(args)

path = ""
# get path from user, or use current working directory by default
if len(args) == 1:
    path = os.getcwd()
else:
    path = args[1]

print("Path", path)


modified_path = path.replace('/','-')
saved_file = open("tree_{}_.txt".format(modified_path), "w+")
saved_file.write(path+"\n\n")


current_dir = os.listdir(path)
for file in current_dir:
    filename = os.fsdecode(file)
    print(filename)
    saved_file.write(filename + "\n")
    
    saved_file.write(str(os.path.isfile(path + "/" + filename)) + "\n")

saved_file.close()
