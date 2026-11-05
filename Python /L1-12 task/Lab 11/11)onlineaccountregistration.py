# Header
print("========================================")
print("       PASSWORD VALIDATION REPORT       ")
print("========================================")

# 1. Take user inputs
username = input("Enter your username: ")
password = input("Enter your password: ")

# Masked password display
masked_password = "*" * len(password)

print("========================================")
print(f"Username: {username}")
print(f"Password: {masked_password}")

print("\n--- Validation Rules ---")

# 2. Check Validation Rules
rule1_len = len(password) >= 8
rule2_digit = any(char.isdigit() for char in password)
rule3_upper = any(char.isupper() for char in password)

# Display individual rule statuses
print(f"[{'PASS' if rule1_len else 'FAIL'}] Minimum 8 characters ({len(password)} characters)")
print(f"[{'PASS' if rule2_digit else 'FAIL'}] At least one digit")
print(f"[{'PASS' if rule3_upper else 'FAIL'}] At least one uppercase letter")

print("\n--- Result ---")

# 3. Final Verdict
if rule1_len and rule2_digit and rule3_upper:
    print("Password is VALID!")
    print(f"Account created successfully for {username}!")
else:
    print("Password is INVALID!")

print("========================================")