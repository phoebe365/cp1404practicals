def main():
    MIN_LENGTH = 8
    password = get_password(MIN_LENGTH)
    print_stars(password)

def print_stars(password):
    print("*" * len(password))

def get_password(MIN_LENGTH):
    password = input("Enter a password: ")
    while len(password) < MIN_LENGTH:
        print(f"Password must be at least {MIN_LENGTH} characters long.")
        password = input("Please enter a valid password: ")
    return password
main()
