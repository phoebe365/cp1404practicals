"""
Emails
Estimate: 30 minutes
Actual:   37 minutes
"""
import re

def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ")
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):

    prefix = email.split('@')[0]
    clean_prefix = re.sub(r'\d+', '', prefix)
    parts = clean_prefix.split('.')
    name = " ".join(parts).title()
    return name


main()