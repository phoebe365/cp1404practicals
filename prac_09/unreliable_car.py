"""Class Unreliable Car"""
from prac_06.car import Car
from random import randint

class UnreliableCar(Car):
    """Class """
    def __init__(self, name, fuel, reliability):
        """Initialise unreliable car instance"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if randint(0,100) < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0.0
        return distance_driven