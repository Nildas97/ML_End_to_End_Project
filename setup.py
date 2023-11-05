# CREATING SETUP FILE FOR THE PROJECT

# importing libraries
from setuptools import setup, find_packages
from typing import List

# setup file items
PROJECT_NAME = "Machine_Learning_End_to_End_Project"
VERSION = "0.0.1"
DESCRIPTION = "this is a end to end machine learning project"
AUTHOR_NAME = "Nilutpal Das"
AUTHOR_EMAIL = "nilutpaldas992@gmail.com"

# requirements file 
REQUIREMENTS_FILE_NAME = "requirements.txt"

HYPHEN_DOT = "-e ."

# defining function to install 
# the libraries from requirements.txt file
def get_requirements_list():
    
    # opening the requirements.txt file
    with open(REQUIREMENTS_FILE_NAME) as requirements_file:

        # reading the requirements file     
        requirements_list = requirements_file.readlines()

        # replacing the "\n" with "" in requirements file 
        requirements_list = [requirements_name.replace("\n", "") for requirements_name in requirements_list]

        # removing the hyphen_dot from the requirements.txt
        if HYPHEN_DOT in requirements_list:
            requirements_list.remove(HYPHEN_DOT)
        return requirements_list

# setup file description
setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR_NAME,
      author_email=AUTHOR_EMAIL,
      packages=find_packages(),
      install_requires=get_requirements_list()
     )