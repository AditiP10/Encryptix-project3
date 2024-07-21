import random
import string

def generate_password(length, use_uppercase, use_numbers, use_special_chars):
    """
    Generate a random password of the specified length and complexity
    """
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
     """
    Main function to prompt user for password length and complexity, and generate password
    """
     print("Welcome to the Password Generator!")
     while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 8:
                print("Password length should be at least 8 characters. Try again!")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a positive integer.") 

     has_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y' 
     has_numbers = input("Include numbers? (y/n): ").lower() == 'y'
     has_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

     password = generate_password(length, has_uppercase, has_numbers, has_special_chars)
     print(f"Generated password: {password}")

if __name__ == "__main__":
    main()