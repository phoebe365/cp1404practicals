"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT" : "Northern Territory", "WA" : "Western Australia",
            "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

for state_code, state_name in CODE_TO_NAME.items():
    print(f"{state_code:<4} is {state_name}")

state_code = input("Enter short state: ").upper()
while state_code != "":
    for state_code in CODE_TO_NAME:
        try:
            print(f"{state_code:<4} is {CODE_TO_NAME[state_code]}")
        except KeyError:
            print(f"Error: {state_code} is not a valid state code.")
        state_code = input("Enter short state: ").upper()

