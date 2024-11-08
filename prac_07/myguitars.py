from prac_06.guitar import Guitar
guitars = []

with open("guitars.csv", "r") as in_file:
    for line in in_file:
        parts = line.strip().split(',')
        year = int(parts[1])
        cost = float(parts[2])
        guitar = Guitar(parts[0], year, cost)
        guitars.append(guitar)

guitar_name = input("Guitar Name: ").title()
while guitar_name != "":
    guitar_year = int(input("Guitar Year: "))
    guitar_cost = float(input("Guitar Cost: "))
    guitar = Guitar(guitar_name, guitar_year, guitar_cost)
    guitars.append(guitar)
    guitar_name = input("Guitar Name: ").title()

guitars.sort()
