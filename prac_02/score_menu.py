"""
CP1404 Practical: Prompt
The menu should have four separate options:

(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit
Handle each of these (except quit) separately, and consider how you can reuse your functions."""

def main():
    print("Welcome to the Score Manager!")
    choice = ""
    score = get_valid_score()  # Initialize score to user input
    while choice != "Q":
        print("\nMenu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")
        choice = input("Choose an option: ").upper()
        if choice == "G":
            score = get_valid_score()  # Get a new valid score
        elif choice == "P":
            if score:
                result = determine_result(score)
                print(f"The result is: {result}")
            else:
                print("Please enter a valid score first.")
        elif choice == "S":
            if score:
                print_stars(score)
            else:
                print("Please enter a valid score first.")
        elif choice == "Q":
            print("Thank you for using the Score Manager! Bye!")
            break
        else:
            print("Invalid input")


def get_valid_score():
     score = float(input("Input score between 0-100 inclusive: "))
     if 0 <= score <= 100:
        return score
     else:
       print("Error: invalid score outside bounds 0:100")
       score = float(input("Input score between 0-100 inclusive: "))

def print_stars(score):
    print("*" * int(score))


def determine_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"
main()
