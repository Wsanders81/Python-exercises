"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    # read words.txt (one word per line). 
    # makes attribute of a list of those words. 
    # print out "[num-of-words-read] words read"
    # create function random() that returns a random word from the list
    def __init__(self, word_list): 
        """Initialize WordFinder class setting arg as variable"""
        self.word_list = word_list
    def random(self): 
        """Select random word from list of words in text file
        Increase counter index to return number of lines read"""
        counter = 0
        
        words = list(open(self.word_list, 'r'))
        for word in range(len(words)): 
            random_word = random.choice(words)
            
            counter += 1
            if words[word] == random_word: 
                print(f"{word} words read")
                return random_word.strip()
        # random_word = random.choice(words)
        # print(random_word, fileinput.lineno())

class SpecialWordFinder(WordFinder): 
    def __init__(self, word_list): 
        super().__init__(word_list)
    def random(self): 
        
        rand = super().random()
        if rand and not rand.startswith('#'):
            return rand 
            