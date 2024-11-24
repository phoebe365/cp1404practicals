class Band:
    """Class band takes the input name"""
    def __init__(self, name=""):
        """Initialise a band object"""
        self.name = name
        self.members = []
        self.member_to_instrument = {}

    def __str__(self):
        """Return a string representation of the band object"""
        return f"{self.name} ({str(self.members).lstrip('[').rstrip(']')})"

    def add(self, musician):
        """Adds a musician to the band object"""
        self.member_to_instrument[musician.name] = musician.instruments
        self.members.append(f"{musician.name} ({musician.instruments})")

    def play(self):
        """Return a string showing which member plays what instrument."""
        for member in self.member_to_instrument:
            if not self.member_to_instrument[member]:
                print(f"{member} needs an instrument!")
            else:
                print(f"{member} is playing: {self.member_to_instrument[member][0]}")