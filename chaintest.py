import unittest
import chains


class ChainTest(unittest.TestCase):
    def assert_differ_by_one(self, word, next):
        character_pairs = zip(word, next)
        def not_equal_chars(pair):
            return pair[0] != pair[1]
        filtered_pairs = list(filter(not_equal_chars, character_pairs))
        self.assertEqual(
            len(filtered_pairs),
            1,
            "filter_pairs: {0}".format(filtered_pairs),
        )

    def test_check_words_in_english(self):
        start_word = 'cat'
        end_word = 'dog'
        words = chains.find_chain(start_word, end_word)

        for word in words:
            with self.subTest(word=word):
                self.assertIn(word, chains.english_dict)

    def test_words_differ_by_one_letter(self):
        start_word = 'cat'
        end_word = 'dog'
        words = chains.find_chain(start_word, end_word)

        word_pairs = zip(words, words[1:])
        for word, next in word_pairs:
            with self.subTest(word=word, next=next):
                self.assert_differ_by_one(word, next)

if __name__ == "__main__":
    unittest.main()