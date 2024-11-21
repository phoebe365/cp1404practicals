"""Project class: includes less than function"""
from datetime import datetime
class Project:
    """Class represents information about a project"""
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Constructor for Project class"""
        self.name = name
        self.start_date = datetime.strptime(start_date, '%d/%m/%Y').date()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """String representation of Project class"""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"


    def __lt__(self, other):
        """Sort the projects by priority"""
        return self.priority < other.priority

