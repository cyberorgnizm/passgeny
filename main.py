#!/usr/bin/env python3
import random
import string
from collections import Counter
"""
This module generates random password of specified length, numbers count and alphabel(uper/lower)
characters given by the user.
"""


def prompt():
    """Prompts users with 'length', 'letters' count and 'numbers' count
    they want for their password
    """
    length = int(input("How long should your password be (in digits)? "))
    while length < 6:
        print("Minumum length for password should be 6")
        length = int(input("How long should your password be (in digits)? "))
    else:
        letters_count, numbers_count = 0, 0
        while letters_count + numbers_count != length:
            letters_count = int(input("How many alphabets should be present (in digits)? "))
            numbers_count = int(input("How many numbers should be present (in digits)? "))
            if letters_count + numbers_count != length:
                print("Please ensure alphabet and numbers count total is equal to length specified")
        return length, letters_count, numbers_count

def extract_characters(text, **kwargs):
    """Extracts an iterable of password characters based on target 'kwargs' specified"""
    text_list = list(text)
    start = text_list.index(kwargs['start'])
    end = text_list.index(kwargs['end'])
    return text_list[start:end+1]

def character_count(text, typeof="str"):
    if typeof == 'str':
        filtered_items = list(filter(lambda char: str.isalpha(char), text))
        return sum(Counter(filtered_items).values())
    elif typeof == 'int':
        filtered_items = list(filter(lambda char: str.isdigit(char), text))
        return sum(Counter(filtered_items).values())
    else:
        return 0

def generate_password(*args):
    """Generates valid password characters to be used for randomly generated password"""
    lowercase = extract_characters(string.ascii_lowercase, start="j", end="y")
    uppercase = extract_characters(string.ascii_uppercase, start="J", end="Y")
    numbers = extract_characters(string.digits, start="4", end="9")

    password = ""
    random_input_types = ['string', 'integer']
    # iteration based on length of password
    for count in range(args[0]):
        
        alphabets_count = character_count(password, typeof="str")
        digits_count = character_count(password, typeof="int")

        if random.choice(random_input_types) == 'integer':
            if digits_count != args[2]:
                password += random.choice(numbers)
                continue
            else:
                password += random.choice([*lowercase, *uppercase])
        else:
            if alphabets_count != args[1]:
                password += random.choice([*lowercase, *uppercase])
            else:
                password += random.choice(numbers)

    return password

if __name__ == '__main__':
    print("Your password =>", generate_password(*prompt()))