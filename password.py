import string 
import getpass

# Minimum length of pass
MIN_LENGTH = 10

def get_password():
    print("Welcome to Eden's secure password checker.")
    print("Enter 'quit' to quit")
    
    pass_input = input("Please enter a password: ")
    return pass_input

# Length function
def check_length(pass_input: list[str]) -> tuple[bool, int]:
    #Analyzes password length against minimum of 10
    #Returns tuple containing bool if length is sufficient or not
    #Returns length of original password
    original_length = len(pass_input)
    long_enough = original_length >= MIN_LENGTH
    return (long_enough, original_length)

def check_upper(pass_input: list[str]) -> bool:
    # checks at least one uppercase 
    return any(char in string.ascii_uppercase for char in pass_input)

def check_lower(pass_input: list[str]) -> bool:
    # checks at least one lowercase 
    return any(char in string.ascii_lowercase for char in pass_input)

def check_digit(pass_input: list[str]) -> bool:
    # checks at least one digit 
    return any(char in string.digits for char in pass_input)

def check_special(pass_input: list[str]) -> bool:
    # checks for at least one special character
    return any(char in string.punctuation for char in pass_input)


## provide report to user 
def print_report(long_enough: bool, length: int, has_upper: bool, has_lower: bool, has_digit: bool, has_special: bool):
    print("\n" + "-"*40)
    print("Password Strength Report")
    print("-"*40)
    print(f"Minimum Length ({MIN_LENGTH}):\t{'✓ Passed' if long_enough else f'Failed. Your password of {length} digits is not long enough'}")
    print(f"Contains Uppercase:\t{'✓ Passed' if has_upper else 'Failed'}")
    print(f"Contains Lowercase:\t{'✓ Passed' if has_lower else 'Failed'}")
    print(f"Contains Digit:\t\t{'✓ Passed' if has_digit else 'Failed'}")
    print(f"Contains Special Char:\t{'✓ Passed' if has_special else 'Failed'}")
    print("-" * 40)

    score = sum([long_enough, has_upper, has_lower, has_digit, has_special])

    if score == 5:
        print("Password Strength: Strong")
    elif score >= 3:
        print("Password Strength: Medium")
    else: 
        print("Password Strength: Weak")
    
    print("-"*40 + "\n")


def main():
    while True:

        pass_input = get_password()
        if pass_input.lower() == 'quit':
            print("Thank you for checking your password. Goodbye!")
            break
        if not pass_input:
            print("Password cannot be empty. Please try again\n")
            continue
            
        pass_input = list(pass_input)
        long_enough, original_length = check_length(pass_input)
        has_upper = check_upper(pass_input)
        has_lower = check_lower(pass_input)
        has_digit = check_digit(pass_input)
        has_special = check_special(pass_input)

        # Pass results to report
        print_report(long_enough, original_length, has_upper, has_lower, has_digit, has_special)


if __name__ == "__main__":
    main()