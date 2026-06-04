# Task 4: Password Generator (CLI)
# Synent Technologies Python Internship

import random
import string

def generate_password(length=12):
    uppercase   = string.ascii_uppercase
    lowercase   = string.ascii_lowercase
    digits      = string.digits
    special     = string.punctuation

    # Ensure at least one character from each category
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special)
    ]

    all_chars = uppercase + lowercase + digits + special
    password += random.choices(all_chars, k=length - 4)

    random.shuffle(password)
    return ''.join(password)

def password_generator():
    print("=" * 40)
    print("  Synent Technologies - Password Generator")
    print("=" * 40)

    while True:
        print("\n1. Generate Password")
        print("2. Exit")

        choice = input("\nEnter choice (1-2): ").strip()

        if choice == '2':
            print("Exiting. Goodbye!")
            break

        if choice != '1':
            print("Invalid choice! Enter 1 or 2.")
            continue

        try:
            length = int(input("Enter password length (min 8, recommended 12-16): "))
            if length < 8:
                print("Minimum length is 8. Setting to 8.")
                length = 8
        except ValueError:
            print("Invalid input! Using default length of 12.")
            length = 12

        password = generate_password(length)
        print(f"\nGenerated Password: {password}")
        print(f"Length: {len(password)} characters")
        print("Strength: STRONG ✓ (Uppercase + Lowercase + Digits + Special chars)")

if __name__ == "__main__":
    password_generator()