def main():
    MIN_LENGTH = 8
    password = input("Enter a password: ")

    while len(password) < MIN_LENGTH:
        print(f"Password must be at least {MIN_LENGTH} characters long.")
        password = input("Please enter a valid password: ")

    print("*" * len(password))
main()
