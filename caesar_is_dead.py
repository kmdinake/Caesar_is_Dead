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


def find_shift(char_with_max_freq, common_character_set):
    global character_set
    shifts = np.array([])
    for cl in common_character_set:
        difference = character_set[character_set.find(char_with_max_freq) - character_set.find(cl)]
        np.append(shifts, difference)


def get_frequency(cipher_text):
    global character_set
    frequencies = np.array([])
    for i in range(len(character_set)):
        for j in range(len(cipher_text)):
            if cipher_text[i] == character_set[i]:
                frequencies[i] += 1
    return frequencies


def get_plain_text(shift, cipher_text):
    for i in range(len(cipher_text)):
        #result += character_set[i + shift]


def find_permutations(cipher_text, character_set):
    pass


def calc_score(plain_text):
    my_file = open('common_3000_words.txt', 'r')
    score = 0
    for word in iter(my_file):
        if word in plain_text:
            score += 1
    my_file.close()
    return score


def decrypt(cipher_text, character_set):
    scores = np.array([])
    plain_texts = find_permutations(cipher_text, character_set)
    for pt in plain_texts:
        np.append(scores, calc_score(pt))
    outputs = np.array([])
    for i in range(len(plain_texts)):
        index = max_score_index(scores)
        np.append(outputs, plain_texts[index])
        scores[index] = 0
    return outputs


def main():
    # read in the encrypted text
    cipher_text = "2XQM5QN7A10QYUXXU104M0P59146T1R5TM4Q5M0PNQOM4QR7X01661NQ5QQ0NA6TQM7564MXUM0S18Q40YQ06M0P2XQM5QNQ8USUXM06"
    character_set = ""
    # read in the character set
    try:
        answer = decrypt(cipher_text, character_set)
        print("Decrypted text: %s", answer)
    except BaseException:
        print("Shucks, failed to decrypt this message... I guess Caesar still lives.")

if __name__ == '__main__':
    main()
