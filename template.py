# PYTHON SCRIPT TO GENERATE PROJECT FOLDERS

# importing libraries
import os
import sys
import logging
from pathlib import Path

# creating while loop to get the input of project_name
while True:
    # asking the project_name
    project_name = input("Enter your project name: ")
    
    # if no project_name entered, then break
    if project_name != "":
        break

# list of files
list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/component/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"config/config.yaml",
    "app.py",
    "main.py",
    "logs.py",
    "exception.py",
    "setup.py"
]

# running a for loop to generate lists_of_files   
for file_path in list_of_files:
    
    # initializing file_path using path libraries
    file_path = Path(file_path)

    # creating file_name and file_dir and splitting them
    # so that each file creates within new folder
    file_dir, file_name = os.path.split(file_path)

    # if file_dir does not exists
    if file_dir != "":
        # create the file_dir, if exists then ignore
        os.makedirs(file_dir, exist_ok=True)

    # if file_path does not exists or if file_path is not available 
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        
        # opening the file_path and generate all the file_dir
        with open(file_path, "w") as f:
            pass
    
    else:
        logging.info("File is already present at: {file_path}")

