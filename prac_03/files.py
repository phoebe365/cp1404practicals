#Question 1
out_file = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=out_file)
out_file.close()

# Question 2
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

#Question 3
with open("numbers.txt", "r") as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
print(number1 + number2)

#Question 4
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        try:
            number = int(line)
            total += number
        except ValueError:
            # Handle the case where the line isn't a valid integer
            print(f"Warning: Could not convert '{line.strip()}' to an integer.")

print(total)