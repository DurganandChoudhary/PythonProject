import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True):
    """Generate a secure random password with customizable options."""
    
    if not (use_uppercase or use_lowercase or use_digits or use_symbols):
        raise ValueError("At least one character type must be selected!")

    char_sets = {
        "uppercase": string.ascii_uppercase if use_uppercase else "",
        "lowercase": string.ascii_lowercase if use_lowercase else "",
        "digits": string.digits if use_digits else "",
        "symbols": string.punctuation if use_symbols else ""
    }

    # Create character pool
    char_pool = "".join(char_sets.values())
    
    if not char_pool:
        raise ValueError("Character pool is empty. Enable at least one option!")

    # Ensure at least one character from each selected set is included
    password = [
        random.choice(char_sets["uppercase"]) if use_uppercase else "",
        random.choice(char_sets["lowercase"]) if use_lowercase else "",
        random.choice(char_sets["digits"]) if use_digits else "",
        random.choice(char_sets["symbols"]) if use_symbols else ""
    ]

    # Fill the rest of the password
    password += random.choices(char_pool, k=length - len(password))

    # Shuffle the password to avoid predictable patterns
    random.shuffle(password)

    return "".join(password)

# Example Usage
if __name__ == "__main__":
    length = int(input("Enter password length: "))
    print("Generated Password:", generate_password(length))
