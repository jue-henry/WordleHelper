from WordBank import WordBank

def main():
    wb = WordBank()
    guess_num = 1
    while len(wb.words) > 1:
        guess = input(f"Guess #{guess_num} (suggestion: {wb.get_suggestion()}): ").lower()
        if not is_valid_word(guess):
            print("Invalid guess. Guesses have to be 5 characters long and can only include alphabet characters.")
            continue
        feedback = input("Please input the feedback of your guess in the form of a 5 character string, " +
                         "where G represents a correct character in the right place," +
                         "Y represents a correct character in the wrong place,and R represents a wrong character: ")
        if not is_valid_feedback(feedback):
            print("Invalid feedback. Feedback strings have to be 5 characters long and can only include G, Y, or R characters.")
            continue
        wb.process_guess(guess, feedback)
        guess_num += 1
        
    if len(wb.words) == 1:
        print(f"Final word: {wb.words[0]}")
    elif feedback == "GGGGG":
        print(f"Final word: {guess}")
    else:
        print("No words match inputted patterns")

def is_valid_word(word: str) -> bool:
    if len(word) == 5 and word.isalpha():
        return True
    return False

def is_valid_feedback(feedback: str) -> bool:
    if len(feedback) == 5 and feedback.isalpha():
        for i in feedback:
            if not i in ['G', 'Y', 'R']:
                return False
        return True
    return False

    
if __name__ == '__main__':
    main()
