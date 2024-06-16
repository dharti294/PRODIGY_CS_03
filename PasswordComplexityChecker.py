def assess_password_strength(password):
    # Criteria for password strength
    min_length = 8
    has_uppercase = any(c.isupper() for c in password)
    has_lowercase = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special_char = any(c for c in password if c.isalnum() is False)

    # Calculate overall strength score
    strength_score = 0
    if len(password) >= min_length:
        strength_score += 1
    if has_uppercase:
        strength_score += 1
    if has_lowercase:
        strength_score += 1
    if has_digit:
        strength_score += 1
    if has_special_char:
        strength_score += 1

    # Provide feedback based on strength score
    if strength_score >= 4:
        return "Strong password! 👍"
    elif strength_score >= 3:
        return "Moderate password. Consider adding more complexity. 💪"
    else:
        return "Weak password. Please choose a stronger one. 🔒"

# Example usage:
user_password = input("Enter your password: ")
feedback = assess_password_strength(user_password)
print(feedback)
