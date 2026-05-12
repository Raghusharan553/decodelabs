import string
import secrets
import math

def calculate_entropy(length, pool_size):
    """
    Calculate password entropy
    E = L × log2(R)
    L = Password Length
    R = Character Pool Size
    """
    entropy = length * math.log2(pool_size)
    return round(entropy, 2)

def generate_password(length):

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    all_characters = lowercase + uppercase + digits + symbols

    password_list = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]
    for _ in range(length - 4):
        password_list.append(secrets.choice(all_characters))
    secrets.SystemRandom().shuffle(password_list)
    password = "".join(password_list)
    return password, len(all_characters)

def password_strength(entropy):
    if entropy < 40:
        return "Weak"
    elif entropy < 60:
        return "Moderate"
    elif entropy < 80:
        return "Strong"
    else:
        return "Very Strong"

def main():
    while True:
        try:
            length = int(input("\nEnter password length (100 - 500): "))
            if length < 100:
                print("Password length must be at least 100.")
                continue
            if length > 500:
                print("Password length should not exceed 500.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter numbers only.")
    password, pool_size = generate_password(length)
    entropy = calculate_entropy(length, pool_size)
    strength = password_strength(entropy)
    
    print("Generated Secure Password")

    print(password)
    print("Password Analysis")
    print(f"Password Length : {length}")
    print(f"Character Pool  : {pool_size}")
    print(f"Entropy         : {entropy} bits")
    print(f"Security Level  : {strength}")
    print("\nPassword generated successfully.")

if __name__ == "__main__":
    main()