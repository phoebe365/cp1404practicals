""" Time estimate: 1.5hrs
Actual time: 2.5 hrs"""

from prac_07.project import Project
from datetime import datetime
MENU = "(L)oad projects\n" \
       "(S)ave projects\n" \
       "(D)isplay projects\n" \
       "(F)ilter projects by date\n" \
       "(A)dd new project\n" \
       "(U)pdate project\n" \
       "(Q)uit"

FILENAME = 'projects.txt'

def main():
    """Print the menu and use the user input to call desired function"""
    projects = []
    print(MENU)
    choice = input(">>>").lower()
    while choice != "q":
        if choice == "l":
            projects = load_projects(FILENAME)
            print("Successfully loaded")
        elif choice == "s":
            save_projects(projects, FILENAME)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_project_by_date(projects)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        else:
            print("Invalid choice.")
        print(MENU)
        choice = input(">>>").lower()
    print("Thank you.")
    save_projects(projects, FILENAME)

def load_projects(FILENAME):
    """Reads file and returns class attributes for each project"""
    projects = []
    try:
        with open(FILENAME, 'r') as in_file:
            in_file.readline()  # Skip header line
            for line in in_file:
                parts = line.strip().split('\t')
                priority = int(parts[2])
                cost_estimate = float(parts[3])
                completion_percentage = int(parts[4])
                project = Project(parts[0], parts[1], priority, cost_estimate, completion_percentage)
                projects.append(project)
    except FileNotFoundError:
        print(f"{FILENAME} not found.")
    return projects


def display_projects(projects):
    """Displays projects broken into complete and incomplete"""
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
    """Updates projects based on user input """
    for i, project in enumerate(projects):
        print(f"{i}. {project}")
    # Get the user's project choice
    update_choice = int(input("Project choice: "))
    selected_project = projects[update_choice]
    print(f"Selected project: {selected_project}")

    new_percentage = int(input("New Percentage: "))

    while new_percentage < 0 or new_percentage > 100:
        print(f"Invalid percentage {new_percentage}, does not lie between 0 and 100")
        new_percentage = int(input("New Percentage: "))
        selected_project.completion_percentage = new_percentage
    try:
        new_priority = int(input("New Priority: "))
        selected_project.priority = new_priority
    except ValueError:
        print(f"Invalid input. Keeping the current priority: {selected_project.priority}")

def filter_project_by_date(projects):
    """Gets user input for a start date and displays the projects after that input date"""
    start_date = input("Generate projects that start after date(dd/mm/yyyy): ")
    start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
    filtered_projects = sorted([project for project in projects if project.start_date >= start_date])

    for project in filtered_projects:
        print(project)



def save_projects(projects, filename):
    """Writes project data to a file."""
    with open(filename, 'w') as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(
                f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.estimate}\t{project.completion}",
                file=out_file)
main()