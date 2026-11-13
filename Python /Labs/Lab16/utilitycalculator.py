print("--------------------------------")
print("Utility Calculator")
print("--------------------------------")

# ==============================================================================
# 1) Modular Arithmetic Engine Functions:-
# ==============================================================================

def format_number(n):
    """
    Helper function to format a number.
    Returns an integer if the value has no decimal part, otherwise a float.
    """
    if n is None:
        return None
    try:
        val = float(n)
        if val.is_integer():
            return int(val)
        return val
    except (ValueError, TypeError):
        return None


def add(a, b):
    """Returns a + b formatted."""
    try:
        val_a = float(a)
        val_b = float(b)
        return format_number(val_a + val_b)
    except (ValueError, TypeError):
        return None


def subtract(a, b):
    """Returns a - b formatted."""
    try:
        val_a = float(a)
        val_b = float(b)
        return format_number(val_a - val_b)
    except (ValueError, TypeError):
        return None


def multiply(a, b):
    """Returns a * b formatted."""
    try:
        val_a = float(a)
        val_b = float(b)
        return format_number(val_a * val_b)
    except (ValueError, TypeError):
        return None


def divide(a, b):
    """
    Returns a / b formatted.
    Defensive check: returns None if b == 0 to prevent crash.
    """
    try:
        val_a = float(a)
        val_b = float(b)
        if val_b == 0:
            return None
        return format_number(val_a / val_b)
    except (ValueError, TypeError):
        return None


def modulus(a, b):
    """
    Returns a % b formatted.
    Defensive check: returns None if b == 0 to prevent crash.
    """
    try:
        val_a = float(a)
        val_b = float(b)
        if val_b == 0:
            return None
        return format_number(val_a % val_b)
    except (ValueError, TypeError):
        return None


def power(base, exp=2):
    """
    Computes base ** exp with a default argument exp=2.
    If exp is omitted, it squares the base.
    """
    try:
        val_base = float(base)
        val_exp = float(exp)
        return format_number(val_base ** val_exp)
    except (ValueError, TypeError):
        return None


# ==============================================================================
# 2) Main Application Loop & Session Management:-
# ==============================================================================

def display_menu():
    """Prints the main interactive menu."""
    print("================================================")
    print("      ENTERPRISE MODULAR UTILITY CALCULATOR by Lovish Goyal  ")
    print("================================================")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus / Remainder (%)")
    print("6. Power / Exponentiation (Default: Square)")
    print("7. View Calculation History")
    print("8. Exit")


def main():
    history = []

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-8): ").strip()

        # Exit program cleanly
        if choice == '8':
            print("\nExiting Enterprise Utility Service. Goodbye!")
            break

        # View Calculation History
        elif choice == '7':
            print("\n--- Session History Ledger ---")
            if not history:
                print("No calculations performed yet.")
            else:
                for idx, entry in enumerate(history, 1):
                    print(f"{idx}. {entry}")
            print()
            continue

        # Operations requiring two numbers (Choices 1-5)
        elif choice in ['1', '2', '3', '4', '5']:
            try:
                num1_raw = input("Enter first number: ")
                num2_raw = input("Enter second number: ")
                num1 = float(num1_raw)
                num2 = float(num2_raw)
            except ValueError:
                print("\n[ERROR] Invalid numeric input. Please try again.\n")
                continue

            num1_s = format_number(num1)
            num2_s = format_number(num2)

            op_map = {
                '1': ('+', add),
                '2': ('-', subtract),
                '3': ('*', multiply),
                '4': ('/', divide),
                '5': ('%', modulus)
            }

            symbol, func = op_map[choice]
            result = func(num1, num2)

            if result is None:
                if choice in ['4', '5'] and num2 == 0:
                    print("\n[ERROR] Division or modulus by zero is undefined.\n")
                else:
                    print("\n[ERROR] Calculation failed.\n")
                continue

            entry = f"{num1_s} {symbol} {num2_s} = {result}"
            history.append(entry)
            print(f"\nResult: {entry}\n")

        # Exponentiation (Choice 6 - supports default exp=2)
        elif choice == '6':
            try:
                base_raw = input("Enter base number: ")
                base = float(base_raw)
            except ValueError:
                print("\n[ERROR] Invalid numeric input for base. Please try again.\n")
                continue

            exp_raw = input("Enter exponent (press Enter to default to 2): ").strip()
            base_s = format_number(base)

            if exp_raw == "":
                result = power(base)
                entry = f"{base_s} ^ 2 = {result}"
            else:
                try:
                    exp = float(exp_raw)
                except ValueError:
                    print("\n[ERROR] Invalid numeric input for exponent. Please try again.\n")
                    continue
                result = power(base, exp)
                entry = f"{base_s} ^ {format_number(exp)} = {result}"

            if result is None:
                print("\n[ERROR] Calculation resulted in an undefined or complex value.\n")
                continue

            history.append(entry)
            print(f"\nResult: {entry}\n")

        else:
            print("\n[ERROR] Invalid option selected. Please choose between 1 and 8.\n")


if __name__ == "__main__":6
main()