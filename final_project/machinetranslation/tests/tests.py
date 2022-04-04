import unittest
import translator


class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(translator.englishToFrench("Hello"), "Bonjour")
        self.assertEqual(translator.englishToFrench(""), "The string was empty")

    def test_frenchToEnglish(self):
        self.assertEqual(translator.frenchToEnglish('Bonjour'), "Hello")
        self.assertEqual(translator.frenchToEnglish(""), "The string was empty")

if __name__ == '__main__':
    unittest.main()