""" Time estimate: 45 mins"""

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
    print("Thank you for using custom-built project management software.")
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
    completed_projects = [project for project in projects if project.completion_percentage == 100]
    print(completed_projects)

def add_new_project(projects):
    pass
def update_project(projects):

    pass
def update_project_by_date(projects):
    pass
def filter_project_by_date(projects):
    pass
def save_projects(projects, filename):
    pass