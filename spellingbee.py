#!/usr/bin/env  python3

import argparse

LEXICON_FILENAME = "lexicon.txt"

class SpellingBeeWord:

    def __init__(self, word: str = "", required_letter: str = "", allowed_letters: str = ""):
        self.word = word
        self.required_letter = required_letter.lower()
        self.allowed_letters = allowed_letters.lower()
        self.points = 0
        self.is_pangram = False

        self.isPangram()
        self.scorePoints()

    def isPangram(self):

        if set(self.word.lower()) >= set(self.required_letter+self.allowed_letters):
            self.is_pangram = True

        return self.is_pangram

    def scorePoints(self):
        """ Returns an estimate of the word's total contribution to the final score. """

        if self.word == "":
            raise ValueError("Word is empty.")

        # 1 point for 4 letter words
        if len(self.word) == 4:
            self.points += 1

        # longer words earn 1 point per letter
        if len(self.word) > 4:
            self.points += len(self.word)

        # 7 extra points if it's a pangram
        if self.is_pangram:
            self.points += 7

class SpellingBeeGame:
    """ Spelling Bee Game. Load the Lexicon, then run it!"""

    def __init__(self, required_letter: str, allowed_letters: str):
        self.required_letter = required_letter
        self.allowed_letters = allowed_letters
        self.total_score_estimate = 0
        self.number_of_pangrams = 0
        self.dictionary = []
        self.answers = []

    def load_lexicon(self, lexicon_filename: str = LEXICON_FILENAME):

        with open(lexicon_filename) as lexicon_file:
            words = lexicon_file.read()
            self.dictionary = words.lower().split("\n")

        print(f"OK - locked n' loaded! 🔫 \nOK -cross checking N possible words: {len(self.dictionary)}")

    def run(self):

        print("INFO - attempting to find solutions...")

        # find possible words
        if len(self.dictionary) != 0:
            allowed_list = list(self.allowed_letters)
            print(f"INFO - allowed letters:\t{allowed_list}")
            print(f"INFO - required letter:\t{self.required_letter}")

            if self.required_letter not in allowed_list:
                allowed_list.append(self.required_letter)

            for word in self.dictionary:
                possible_answer = False

                if self.required_letter in word:
                    possible_answer = True

                    for letter in word:
                        if letter not in allowed_list:
                            possible_answer = False

                if possible_answer and len(word) >= 4:
                    # found a match!
                    sbw = SpellingBeeWord(word, self.required_letter, self.allowed_letters)
                    self.answers.append(sbw)
                    if sbw.is_pangram:
                        self.number_of_pangrams += 1


        print("🐝 - DONE! Here are your possible answers:")
        # estimate total score
        for ans in self.answers:
            self.total_score_estimate += ans.points

        for ans in self.answers:
            if ans.is_pangram:
                print(f"\t{ans.word} - {ans.points} points\t\t<- is a pangram!")
            else:
                print(f"\t{ans.word} - {ans.points} points")

        print(f"OK - found {len(self.answers)} possible words! {self.number_of_pangrams} are pangrams!")
        print(f"OK - estimated total score: {self.total_score_estimate}")


if __name__ == "__main__":
    desc = '🐝 NYT Spelling Bee solutions\' finder!'

    parser = argparse.ArgumentParser(description=desc, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('required_letter', type=str, nargs='?', default='u', help='required letter')
    parser.add_argument('allowed_letters', type=str, nargs='?', default='iptnea', help='allowed letters (in any order)')

    args = parser.parse_args()
    game = SpellingBeeGame(args.required_letter.lower(), args.allowed_letters.lower())
    game.load_lexicon()
    game.run()