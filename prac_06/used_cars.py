"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)
    my_limo = Car(100)
    my_limo.add_fuel(20)
    my_limo.drive(115)

    # test cars
    car_1 = Car("Toyota", 60)
    car_2 = Car("Lexus", 100)
    car_3 = Car("Honda", 180)
    print(car_1)
    print(car_2)
    print(car_3)
    print(f"Limo has fuel: {my_limo.fuel}")
main()