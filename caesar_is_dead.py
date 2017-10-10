"""
Using frequency analysis, attempt to decrypt any caesar's within well capabilities
"""
import sys
import numpy as np


def max_score_index(scores):
    h_index = -1
    highest = -np.Infinity
    for s in range(len(scores)):
        if scores[s] > highest:
            h_index = s
            highest = scores[s]
    return h_index


def find_shift(character, common_character_set):
    pass


def get_frequency(character, cipher_text):
    pass


def get_plain_text(shift, cipher_text):
    pass


def find_permutations(cipher_text, character_set):
    pass


def decrypt(cipher_text, character_set):
    scores = np.array()
    plain_texts = find_permutations(cipher_text, character_set)
    for pt in plain_texts:
        scores.append(calc_score(pt))
    index = max_score_index(scores)
    return plain_texts[index]


def main():
    # read in the encrypted text
    cipher_text = ""
    character_set = ""
    # read in the character set
    answer = decrypt(cipher_text, character_set)
    print("Decrypted text: %s", answer)


if __name__ == '__main__':
    main()
