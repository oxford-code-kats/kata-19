with open('/usr/share/dict/words', 'r') as word_file:
    english_dict = {line.rstrip().lower() for line in word_file}

def find_chain(start_word, end_word):
    chain = [start_word, end_word]
    return chain