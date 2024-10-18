import re

def password_strength_checker(password):
    
    score = 0
    feedback = []

    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Add at least one number.")

   
    if re.search(r'[\W_]', password):
        score += 1
    else:
        feedback.append("Add at least one special character (e.g., @, #, $, %).")

  
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return {"strength": strength, "feedback": feedback}


def main():
    while True:
        password = input("Enter your password: ")
        result = password_strength_checker(password)

        print(f"Password strength: {result['strength']}")
        if result['strength'] == "Weak":
            print("Suggestions for improvement:")
            for item in result['feedback']:
                print(f"- {item}")
            print("Please try again.\n")
        else:
            print("Your password is strong enough!")
            break  # Exit the loop when password is strong or medium


if __name__ == "__main__":
    main()
