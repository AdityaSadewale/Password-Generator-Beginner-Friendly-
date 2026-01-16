# this an Advanced Password Generator (Beginner Friendly)
'''
✔ Choose password length
✔ Choose what to include (numbers, symbols)
✔ Strong password (at least 1 uppercase, lowercase, digit, symbol)
✔ Option to generate multiple passwords
✔ Uses secure method
'''
import string
import secrets

print("=== PASSWORD GENERATOR ===")

while True:
    length = int(input("\nEnter password length (minimum 8): "))

    if length < 8:
        print("❌ Password must be at least 8 characters!")
        continue

    use_digits = input("Include numbers? (y/n): ").lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").lower() == "y"

    characters = string.ascii_lowercase + string.ascii_uppercase

    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    # Ensure strong password
    password = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase)
    ]

    if use_digits:
        password.append(secrets.choice(string.digits))
    if use_symbols:
        password.append(secrets.choice(string.punctuation))

    while len(password) < length:
        password.append(secrets.choice(characters))

    secrets.SystemRandom().shuffle(password)

    final_password = "".join(password)
    print("\n✅ Your strong password is:")
    print(final_password)

    again = input("\nGenerate another password? (y/n): ")
    if again.lower() != "y":
        print("\nThank you for using Password Generator 🔐")
        break


# Run Command in VS Code Terminal
# python adv_pass_gen.py
