"""15. Write a Python module named file_operations.py with functions for reading, writing, and appending
data to a file."""

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."
    except IOError:
        return "Error reading file."

def write_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            file.write(data)
            return "Write operation successful."
    except IOError:
        return "Error writing to file."

def append_to_file(file_path, data):
    try:
        with open(file_path, 'a') as file:
            file.write(data)
            return "Append operation successful."
    except IOError:
        return "Error appending to file."

