import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"

password = ""

password += random.choice(lower)
password += random.choice(upper)
password += random.choice(numbers)

characters = lower + upper + numbers

for i in range(5):
    password += random.choice(characters)

password = list(password)
random.shuffle(password)

password = "".join(password)

print("Password:", password)