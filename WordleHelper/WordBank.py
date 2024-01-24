class WordBank():
    def __init__(self):
        with open('words.txt') as word_file:
            self.words = list(word_file.read().split())
           
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
