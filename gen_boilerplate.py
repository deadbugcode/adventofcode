from datetime import datetime
import os
import shutil
import sys

def main():
    # Generate folder name
    year =  datetime.today().strftime("%Y") 
    day = datetime.today().strftime("%d") 
    script_folder_name = os.path.dirname(os.path.abspath(__file__))
    folder_name = os.path.join(script_folder_name, year, day)
    py_filename = os.path.join(folder_name, "aoc" + day + ".py")
    print(py_filename)

    if os.path.exists(folder_name) and os.path.isdir(folder_name):
        print("Directory already exists.")
        return

    # Make folder
    os.makedirs(folder_name)

    # Make blank files
    for blank_file in ['example.txt', 'input.txt']:
        open(os.path.join(folder_name, blank_file), 'w').close()

    # Copy boilerplate python file
    shutil.copyfile(os.path.join(script_folder_name, "template.py"), py_filename) 


main()
