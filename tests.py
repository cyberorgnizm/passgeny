import string
import unittest
from collections import Counter
from main import extract_characters, generate_password


class TestPasswordGenerator(unittest.TestCase):

    def setUp(self):
        self.length = 10
        self.alphabets = 3
        self.digits = 7

    def test_extract_characters(self):
        """test if character slicing extracts within given range"""
        letters = extract_characters(string.ascii_letters, start="a", end="z")
        self.assertEqual(letters, list(string.ascii_lowercase))
    
    def test_generated_password_length(self):
        """test if length of password match length specified"""
        password = generate_password(self.length, self.alphabets, self.digits)
        self.assertEqual(len(password), self.length)

    def test_generated_password_valid(self):
        """test if number of alphabets and digits specified is present in generated password"""
        password = generate_password(self.length, self.alphabets, self.digits)
        digits_count = sum(Counter(list(filter(lambda item: str.isdigit(item), password))).values())
        alphabets_count = sum(Counter(list(filter(lambda item: str.isalpha(item), password))).values())

        self.assertEqual(alphabets_count, self.alphabets)
        self.assertEqual(digits_count, self.digits)

if __name__ == '__main__':
    unittest.main()