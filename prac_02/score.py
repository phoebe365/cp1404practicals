"""
CP1404/CP5632 - Practical
Program to determine score status with functions
"""
import random

def main():
    score = float(input("Enter score: "))
    if score < 0 or score > 100:
        print("Invalid score")
    else:
        result = determine_result(score)
        print(result)

    # Generate a random score and print the result
    random_score = random.uniform(0, 100)  # Generate random float between 0 and 100
    print(f"Random score: {random_score:.2f}")
    print(determine_result(random_score))  # Get the result for the random score

def determine_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()
