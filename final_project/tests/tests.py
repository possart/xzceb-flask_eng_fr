"""Test module for translator"""
import unittest

from machinetranslation.translator import english_to_french, french_to_english

class Test(unittest.TestCase):
    def test_english_to_french(self):
        """Test translator.english_to_french"""
        self.assertEqual(english_to_french('hello'),'bonjour')
        self.assertNotEqual(english_to_french('hello'),'salut')

    def test_french_to_english(self):
        """Test translator.english_to_french"""
        self.assertEqual(french_to_english('bonjour'),'hello')
        self.assertNotEqual(french_to_english('salut'),'hello')

if __name__ == '__main__':
    unittest.main()