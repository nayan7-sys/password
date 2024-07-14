import random
import string

def generate_password(length, num_letters, num_digits, num_symbols):
    """Generate a random password based on specified criteria."""
    if num_letters + num_digits + num_symbols > length:
        raise ValueError("Sum of letters, digits, and symbols exceeds password length.")
    
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    
    password_letters = random.choices(letters, k=num_letters)
    password_digits = random.choices(digits, k=num_digits)
    password_symbols = random.choices(symbols, k=num_symbols)
    
    password_list = password_letters + password_digits + password_symbols
    random.shuffle(password_list)
    
    return ''.join(password_list)

def main():
    """Main function to interact with the user and generate a password."""
    print("Welcome to the Password Generator!")

    while True:
        try:
            # Getting inputs
            length = int(input("Enter the total length of the password: "))
            num_letters = int(input("Enter the number of letters in the password: "))
            num_digits = int(input("Enter the number of digits in the password: "))
            num_symbols = int(input("Enter the number of symbols in the password: "))
        
            # Validate inputs
            if length <= 0:
                raise ValueError("Password length must be a positive integer.")
            if num_letters < 0 or num_digits < 0 or num_symbols < 0:
                raise ValueError("Number of letters, digits, and symbols must be non-negative.")
            if num_letters + num_digits + num_symbols > length:
                raise ValueError("Sum of letters, digits, and symbols exceeds total length.")

            # Generating the password
            password = generate_password(length, num_letters, num_digits, num_symbols)
            print(f"\nGenerated password: {password}")
            
            # Asking to generate another password?
            continue_input = input("\nDo you want to generate another password? (yes/no): ").strip().lower()
            if continue_input != 'yes':
                break

        except ValueError as e:
            print(f"Invalid input: {e}. Please enter valid numeric values.")

if __name__ == "__main__":
    main()
