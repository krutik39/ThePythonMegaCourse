import datetime

r"""
This script creates an empty file
"""

filename=datetime.datetime.now()

def create_file():
    """This function creates an empty file"""
    with open(filename.strftime("%Y-%m-%d-%H-%M-%S")+".txt","w") as file:
        file.write("") #Writing an empty string.

create_file()
