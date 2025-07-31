import random
import string

def generate_password(length):
    if length < 10:
        raise ValueError("Password length is too short, try a longer password")
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Random Password Generator\n")

    try:
        length = int(input("Enter desired password length(min 10): "))
        password = generate_password(length)
        print(f"\nYour random password is:\n{password}")
    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()