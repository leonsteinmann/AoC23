import os

def get_input(day):
    inputs_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'inputs'))
    filename = os.path.join(inputs_folder, f"{day:02}.txt")
    try:
        with open(filename, 'r') as file:
            return file.read().strip().splitlines()  # Read lines into a list
    except FileNotFoundError:
        print(f"Input file for day {day} not found.")
        return None


def get_input_string(day):
    inputs_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'inputs'))
    filename = os.path.join(inputs_folder, f"{day:02}.txt")
    try:
        with open(filename, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Input file for day {day} not found.")
        return None