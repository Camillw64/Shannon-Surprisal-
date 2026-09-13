import secrets
import string

NUM_PASSWORDS = 10_000
PASSWORD_LENGTH = 12

SPECIAL_CHARACTERS = "!@#$%&*-_+="
CHARACTERS = string.ascii_uppercase + string.ascii_lowercase + string.digits + SPECIAL_CHARACTERS

passwords = set()

while len(passwords) < NUM_PASSWORDS:
    password = "".join(secrets.choice(CHARACTERS) for _ in range(PASSWORD_LENGTH))
    passwords.add(password)

with open("passwords.csv", "w", newline="") as file:
    for password in passwords:
        file.write(password + "\n")

print(f"Generated {len(passwords):,} unique passwords.")
print("Saved to passwords.csv")