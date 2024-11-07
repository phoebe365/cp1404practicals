from prac_06.guitar import Guitar

def main():

    guitars = []
    #guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    #guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("My guitars!")
    name = input("Name: ")

    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar_input = Guitar(name, year, cost)
        guitars.append(new_guitar_input)
        print(new_guitar_input, "added.")
        name = input("Name: ")

    if guitars:
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = " (vintage)" # ensures that vintage guitars are labelled
            print("Guitar {0}: {1.name:>20} ({1.year}), worth ${1.cost:10,.2f}{2}".format(i, guitar, vintage_string))
    else:
        print("No guitars owned.")

if __name__ == '__main__':
    main()