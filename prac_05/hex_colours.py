
COLOUR_TO_CODE= {"Amethyst": "#9966cc", "Baby Pink": "#f4c2c2","Canary Yellow": "#ffef00", "Cosmic Latte": "#fff8e7",
                 "Earth Yellow": "#e1a95f", "Granny Smith Apple": "#a8e4a0", "Lavender Blue": "#ccccff", "Moss Green": "#8a9a5b",
                 "SaddleBrown": "#8b4513","Zomp": "#39a78e" }
print(COLOUR_TO_CODE)
max_colour_len = max(len(colour_name) for colour_name in COLOUR_TO_CODE)

print(COLOUR_TO_CODE)

# Loop to handle user input and display colour codes
colour_name = input("Enter a colour name: ").title()

while colour_name != "":
    if  colour_name in COLOUR_TO_CODE:
         print(f"{colour_name:<{max_colour_len}} is {COLOUR_TO_CODE[colour_name]}")
    else:
         print(f"Error: {colour_name} is not a valid colour.")

    colour_name = input("Enter a colour name (or press Enter to quit): ").title()
