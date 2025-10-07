import string 
from flask import Flask, render_template, request

# Create Flask App 
app = Flask(__name__)

# Minimum length of pass
MIN_LENGTH = 10


# Length function
def check_length(password: list[str]) -> tuple[bool, int]:
    #Analyzes password length against minimum of 10
    #Returns tuple containing bool if length is sufficient or not
    #Returns length of original password
    original_length = len(password)
    long_enough = original_length >= MIN_LENGTH
    return (long_enough, original_length)

def check_upper(password: list[str]) -> bool:
    # checks at least one uppercase 
    return any(char in string.ascii_uppercase for char in password)

def check_lower(password: list[str]) -> bool:
    # checks at least one lowercase 
    return any(char in string.ascii_lowercase for char in password)

def check_digit(password: list[str]) -> bool:
    # checks at least one digit 
    return any(char in string.digits for char in password)

def check_special(password: list[str]) -> bool:
    # checks for at least one special character
    return any(char in string.punctuation for char in password)


## provide report to user 
def generate_report(long_enough: bool, length: int, has_upper: bool, has_lower: bool, has_digit: bool, has_special: bool):
    report_lines = []
    report_lines.append((f"Minimum Length ({MIN_LENGTH})", long_enough, f"{'✓ Passed' if long_enough else f'✗ Failed (is {length})'}"))
    report_lines.append(("Contains Uppercase", has_upper, f"{'✓ Passed' if has_upper else '✗ Failed'}"))
    report_lines.append(("Contains Lowercase", has_lower, f"{'✓ Passed' if has_lower else '✗ Failed'}"))
    report_lines.append(("Contains Digit", has_digit, f"{'✓ Passed' if has_digit else '✗ Failed'}"))
    report_lines.append(("Contains Special Char", has_special, f"{'✓ Passed' if has_special else '✗ Failed'}"))


    score = sum([long_enough, has_upper, has_lower, has_digit, has_special])

    if score == 5:
        strength = "Password Strength: Strong"
    elif score >= 3:
        strength = "Password Strength: Medium"
    else: 
        strength = "Password Strength: Weak"
    
    return report_lines, strength

@app.route('/', methods=['GET', 'POST'])
def home():
    report_data = None
    strength = None
    pass_input = ""
    
    if request.method == 'POST':
        pass_input = request.form.get('pass_input)

        if pass_input:
            
            long_enough, original_length = check_length(pass_input)
            has_upper = check_upper(pass_input)
            has_lower = check_lower(pass_input)
            has_digit = check_digit(pass_input)
            has_special = check_special(pass_input)

            # Pass results to report function
            report_data, strength = generate_report(long_enough, original_length, has_upper, has_lower, has_digit, has_special)
    
    return render_template('index.html', report_data=report_data, strength=strength, pass_input=pass_input)


if __name__ == "__main__":
    app.run(debug=True, port=8080)