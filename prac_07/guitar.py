class Guitar:
    """Guitar class takes the inputs name, year, and cost."""
    def __init__(self, name = "", year = 0, cost = 0):
        """Construct a Guitar object"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the Guitar object"""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __lt__(self, other):
        """Compare guitars by their year for sorting (oldest to newest)."""
        return self.year < other.year

    def get_age(self):
        """Return the age of the Guitar."""
        current_guitar_age = 2024 - int(self.year)
        print(f"In 2024 the {self.name} is: 2024 - {self.year} = {current_guitar_age}")
        return current_guitar_age

    def is_vintage(self):
        """Return vintage if the guitar is 50 or more years old"""
        age = self.get_age()
        if age >= 50:
            return f"{self.name} is a vintage guitar."
        else:
            return f"{self.name} is not a vintage guitar."