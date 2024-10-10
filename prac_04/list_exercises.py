def main():
    numbers = []

    for i in range(5): # Prompt the user for 5 numbers
        number = float(input(f"Number {i + 1}: "))
        numbers.append(number)

    # Output information
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers):.2f}")

main()
