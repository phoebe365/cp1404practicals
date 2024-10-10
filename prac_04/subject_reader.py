"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"
def main():
    data = load_data()
    print(data)
    display_subject_details(data)

def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subject_data = []  # List to hold all the subject information

    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))
        line = line.strip()
        parts = line.split(',')
        print(parts)
        parts[2] = int(parts[2]) # Convert the student number (3rd part) to an integer
        print(parts)
        print("----------")
        subject_data.append(parts)
    input_file.close()
    return subject_data

def display_subject_details(subject_data):
    for subject in subject_data:
        subject_code, lecturer, student_count = subject # Unpack the subject list
        print(f"{subject_code} is taught by {lecturer} and has {student_count} students")

main()
