import unittest
import chains

with open('/usr/share/dict/words', 'r') as word_file:
    english_dict = {line.rstrip().lower() for line in word_file}

class ChainTest(unittest.TestCase):
    def test_check_words_in_english(self):
        start_word = 'cat'
        end_word = 'dog'
        words = chains.find_chain(start_word, end_word)

        for word in words:
            with self.subTest(word=word):
                self.assertIn(word, english_dict)

    def test_words_differ_by_one_letter(self):
        pass

if __name__ == "__main__":
    unittest.main()