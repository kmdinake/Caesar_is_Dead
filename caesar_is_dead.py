"""
Using frequency analysis, attempt to decrypt any caesar's within well capabilities
"""
import sys
import numpy as np

character_set = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ";
common_character_set = "ETAOINSRHLDCUMFPGWYBVKXJQZ";

def max_score_index(scores):
    h_index = -1
    highest = -np.Infinity
    for s in range(len(scores)):
        if scores[s] > highest:
            h_index = s
            highest = scores[s]
    return h_index


def find_shift(character, common_character_set, frequencies):
        return character - common_character_set[max(frequencies)]


def get_frequency(character, cipher_text):
    frequencies = np.array()
    for i in range(len(cipher_text)):
        for j in range(len(cipher_text)):
            if cipher_text[i] == character[i]:
                frequencies[i] += 1
    return frequencies


def get_plain_text(shift, cipher_text):
    for i in range(len(cipher_text)):
        #result += character_set[i + shift]


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
