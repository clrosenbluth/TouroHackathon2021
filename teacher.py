import os.path
from os import path
import os


def get_info():
    print("Welcome to Speed Type!")

    # Get information - teacher name, teacher class, and input file name
    teacher_name = input("Please enter your name: ")
    class_name = input("Please enter the name of the class: ")

    while True:
        file_name = input("Please enter the name of the input file: ")

        # Check that the file exists
        if not path.exists(file_name):
            print("Sorry, that file doesn't appear to exists")
            continue

        if not path.isfile(file_name):
            print("Sorry, that doesn't appear to be a file")
            continue

        if not file_name[-4:] == '.txt':
            print("Sorry, that doesn't appear to be a text file")
            continue

        if os.stat(file_name).st_size == 0:
            print("Sorry, that file appears to be empty")
            continue

        break

    return teacher_name, class_name, file_name

