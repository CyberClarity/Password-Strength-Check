import re

def check_password_strength(password):
    # Initialize score and feedback list
    score = 0
    feedback = []

    # Check length
    if len(password) >= 12:
        score += 2
        feedback.append("✅ Good length (12+ characters).")
    elif len(password) >= 8:
        score += 1
        feedback.append("🟡 Decent length (8-11 characters), but longer is better.")
    else:
        feedback.append("❌ Too short! Use at least 8 characters.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
        feedback.append("✅ Contains lowercase letters.")
    else:
        feedback.append("❌ Add lowercase letters.")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
        feedback.append("✅ Contains uppercase letters.")
    else:
        feedback.append("❌ Add uppercase letters.")

    # Check for digits
    if re.search(r"\d", password):
        score += 1
        feedback.append("✅ Contains numbers.")
    else:
        feedback.append("❌ Add numbers.")

    # Check for symbols
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
        feedback.append("✅ Contains special symbols.")
    else:
        feedback.append("❌ Add special symbols (!@#$ etc.).")

    # Calculate overall result
    if score >= 6:
        strength = "🔒 Very Strong"
    elif score >= 4:
        strength = "🟢 Strong"
    elif score >= 3:
        strength = "🟡 Moderate"
    else:
        strength = "🔴 Weak"

    # Print results
    print("\n--- Password Analysis ---")
    print(f"Password: {password}")
    print(f"Strength: {strength}")
    print("\nDetails:")
    for item in feedback:
        print(f"- {item}")
    print("-------------------------\n")

if __name__ == "__main__":
    print("🔑 Welcome to the Python Password Strength Checker 🔑\n")
    password_input = input("Enter the password to evaluate: ")
    check_password_strength(password_input)
