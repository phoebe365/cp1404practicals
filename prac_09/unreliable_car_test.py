from prac_09.unreliable_car import UnreliableCar


def main():
    """Test some UnreliableCars."""
    good_car = UnreliableCar("Mostly Good", 100, 85)
    bad_car = UnreliableCar("Dodgy", 100, 9)

    for i in range(1, 10):
        print(f"Attempting to drive {i}km:")
        print(f"{good_car.name:12} drove {good_car.drive(i):2}km")
        print(f"{bad_car.name:12} drove {bad_car.drive(i):2}km")

    # print the final states of the cars
    print(good_car)
    print(bad_car)


main()