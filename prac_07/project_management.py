""" Time estimate: 1.5hrs"""

from prac_07.project import Project
from datetime import datetime

MENU = "(L)oad projects\n" \
       "(S)ave projects\n" \
       "(D)isplay projects\n" \
       "(F)ilter projects by date\n" \
       "(A)dd new project\n" \
       "(U)pdate project\n" \
       "(Q)uit"

FILENAME = 'project.txt'

def main():
    """Print the menu and use the user input to call desired function"""
    projects = load_projects(FILENAME)
    print(MENU)
    choice = input(">>>").lower()
    while choice != "q":
        if choice == "l":
            print("Successfully loaded")
        elif choice == "s":
            print("Successfully Saved")
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_project_by_date(projects)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        else:
            print("invalid choice")
        print(MENU)
        choice = input(">>>").lower()
    print("Thank you.")
    save_projects(projects, FILENAME)

def load_projects(filename):
    projects = []
    with open(filename, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percentage = int(parts[4])
            project = Project(parts[0], parts[1], priority, cost_estimate, completion_percentage)
            projects.append(project)
    return projects


def display_projects(projects):
    completed_projects = sorted([project for project in projects if project.completion_percentage == 100])
    incomplete_projects = sorted([project for project in projects if project.completion_percentage < 100])


    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project}")

def add_new_project(projects):
    """Add a new project to the list through user input."""
    print("To add a new project input the following details:")
    name = input("Name: ").title()
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    completion = int(input("Completion percentage: "))
    project = Project(name, start_date, priority, cost_estimate, completion)
    projects.append(project)


def update_project(projects):

    pass
def update_project_by_date(projects):
    pass
def filter_project_by_date(projects):
    pass
def save_projects(projects, filename):
    pass