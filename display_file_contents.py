def display_file_contents(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                print(line, end='')  
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
    except IOError as e:
        print(f"An IOError occurred: {e}")

if __name__ == "__main__":
    display_file_contents(file_name)