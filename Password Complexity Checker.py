import re
import logging

logging.basicConfig(filename='password_checker.log', level=logging.INFO)

def check_password_complexity(password, min_length=8):
    feedback = ""

    length_criteria = len(password) >= min_length
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_character_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_character_criteria])

    if score == 5:
        feedback = "Very Strong"
    elif score >= 3:
        feedback = "Strong"
    elif score >= 2:
        feedback = "Moderate"
    elif score >= 1:
        feedback = "Weak"
    else:
        feedback = "Very Weak"

    logging.info(f"Password '{password}' strength: {feedback}")

    return feedback

def suggest_password_improvement(password):
    suggestions = []
    if len(password) < 8:
        suggestions.append("Increase password length to at least 8 characters.")
    if not bool(re.search(r'[A-Z]', password)):
        suggestions.append("Include at least one uppercase letter.")
    if not bool(re.search(r'[a-z]', password)):
        suggestions.append("Include at least one lowercase letter.")
    if not bool(re.search(r'\d', password)):
        suggestions.append("Include at least one digit.")
    if not bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)):
        suggestions.append("Include at least one special character (!@#$%^&*(),.?\":{}|<>).")
    return suggestions

def main():
    print("Welcome to the Password Complexity Checker")
    print("------------------------------------------")
    password = input("Enter your password: ")

    strength = check_password_complexity(password)
    print(f"The strength of your password is: {strength}")

    if strength == "Weak" or strength == "Very Weak":
        print("Suggestions to improve password:")
        for suggestion in suggest_password_improvement(password):
            print("-", suggestion)

if __name__ == "__main__":
    main()
