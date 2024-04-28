import random
import pyperclip
import time

list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"

def generate_random_string(length, characters):
    return ''.join(random.choice(characters) for _ in range(length))

random_string = generate_random_string(int(input("Enter length: ")), list)
print("Copied to clipboard!")
pyperclip.copy(random_string)
time.sleep(0.5)
print("Press Enter to exit...")
input()
