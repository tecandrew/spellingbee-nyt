#!/usr/bin/env  python3

import argparse

LEXICON_FILENAME = "lexicon.txt"

def spellingBee_predict_score(match_list: list, allowed_letters: list):
    score = 0
    for m in match_list:
        all_in = True
        for i in allowed_letters:
            if i not in m:
                all_in = False
        if all_in == False:
            score += 1
        if all_in == True:
            score += 3

    return score

def spellingBee_find_matches(allowed_letters: str, required_letter: str, lexicon: list):
    allowed_list = list(allowed_letters)
    print("---")
    print(f"allowed letters: {allowed_list}")
    print(f"required letter: {required_letter}")

    if required_letter not in allowed_list:
        allowed_list.append(required_letter)

    match_words= []

    for word in lexicon:
        no_good = True
        if required_letter in word:
            no_good = False
            for z in word:
                if z not in allowed_list:
                    no_good = True
        if no_good == False and len(word) > 4:
            match_words.append(word)

    score = spellingBee_predict_score(match_words, allowed_list)
    return match_words, score

def gen_possible_solutions(required_letter: str , allowed_letters: str):
    entire_lexicon = []
    print(f'creating possibilities for: [{required_letter}, {allowed_letters}]')

    print("loading entire lexicon...")
    with open(LEXICON_FILENAME) as lexicon_file:
        words = lexicon_file.read()
        entire_lexicon = words.lower().split("\n")

    print(f"OK - locked n' loaded! cross checking N possible words: {len(entire_lexicon)}")
    print("attempting to find solutions...")
    match_words, score = spellingBee_find_matches(allowed_letters, required_letter, entire_lexicon)

    print(f"OK - found {len(match_words)} possible words!")

    for m in match_words:
        print(f"{m}")

    print(f"OK - predicted score: {score}")

if __name__ == "__main__":
    desc = '🐝 NYT Spelling Bee solutions\' finder!'

    parser = argparse.ArgumentParser(description=desc, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('required_letter', type=str, nargs='?', default='u', help='required letter')
    parser.add_argument('allowed_letters', type=str, nargs='?', default='iptnea', help='allowed letters (in any order)')

    args = parser.parse_args()
    gen_possible_solutions(args.required_letter, args.allowed_letters)