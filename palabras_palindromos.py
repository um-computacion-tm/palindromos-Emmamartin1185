import unittest


def is_palindrome(palabra):
    palabra2 = palabra[::-1]
    if palabra == palabra2:
        return True
    return False


   


class TestIsPalindrome(unittest.TestCase):
    def test_with_a(self):
        input = "a"
        result = is_palindrome(input)
        self.assertTrue(result)

    def test_with_ala(self):
        input = "ala"
        result = is_palindrome(input)
        self.assertTrue(result)

    def test_with_neuquen(self):
        input = "neuquen"
        result = is_palindrome(input)
        self.assertTrue(result)

    def test_with_hola(self):
        input = "hola"
        result = is_palindrome(input)
        self.assertFalse(result)


unittest.main()