# points assigned to letters based on frequency of use in English language
LETTER_RANKINGS = {
    'e': 10,
    't': 9,
    'a': 8,
    'o': 7.5,
    'i': 7,
    'n': 7,
    's': 6.5,
    'h': 6,
    'r': 6,
    'd': 4.5,
    'l': 4,
    'u': 3,
    'c': 2.5,
    'm': 2.5,
    'f': 2.5,
    'w': 2,
    'g': 2,
    'y': 2,
    'p': 1.5,
    'b': 1.5,
    'v': 1,
    'k': 0.5,
    'x': 0.5,
    'j': 0.5,
    'q': 0.5,
    'z': 0.5
}

class WordBank():
    def __init__(self):
        with open('words.txt') as word_file:
            self.words = word_file.read().split()
            self.words.sort(key= WordBank.get_score, reverse = True)
           
    # method to remove words that do not match the pattern provided by the guess and feedback strings
    def process_guess(self, guess: str, feedback: str) -> None:
        try:
            self.words.remove(guess)
        except ValueError:
            pass
        finally:  
            for i in range(len(guess)):
                if feedback[i] == 'G':
                    self.words = list(filter(lambda x:x[i] == guess[i], self.words))
                elif not guess[i] in guess[:i]:
                    if feedback[i] == 'Y':
                        self.words = list(filter(lambda x:x[i] != guess[i] and guess[i] in x, self.words))
                    else:
                        self.words = list(filter(lambda x:not guess[i] in x, self.words))
        print(self.words)
        
    def get_suggestion(self) -> str:
        return self.words[0] if len(self.words) > 0 else ""

    # method to score words based on frequency of the letters used in the English language
    def get_score(word: str) -> int:
        score = 0
        for i in range(len(word)):
            # skips duplicate letters in order to increase variety of letters for suggestion
            if not word[i] in word[:i]:
                score += LETTER_RANKINGS[word[i]]
        return score