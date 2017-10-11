"""
Using frequency analysis, attempt to decrypt any caesar's within well capabilities
"""
import numpy as np


character_set = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
common_character_set = "EeTtAaOoIiNnSsRrHhLlDdCcUuMmFfPpGgWwYyBbVvKkXxJjQqZz"


def get_max_index(scores):
    h_index = -1
    highest = -np.Infinity
    for s in range(len(scores)):
        if scores[s] > highest:
            h_index = s
            highest = scores[s]
    return h_index


def find_shifts(char_with_max_freq, char_set, common_char_set):
        shifts = []
        for cl in common_char_set:
            x = char_set.find(char_with_max_freq)
            y = char_set.find(cl)
            diff = x - y
            shifts.append(diff)
        return shifts


def get_frequency(cipher_text, char_set):
    frequencies = np.zeros(len(char_set))
    for j in range(len(char_set)):
        for i in range(len(cipher_text)):
            if cipher_text[i] == char_set[j]:
                frequencies[j] += 1
    return frequencies


def get_plain_text(shift, cipher_text, char_set):
    result = ""
    for c in cipher_text:
        index = char_set.find(c)
        result += char_set[(index - shift) % len(char_set)]
    return result


def find_permutations(cipher_text, char_set, common_char_set):
    frequencies = get_frequency(cipher_text, char_set)
    index = get_max_index(frequencies)
    shifts = find_shifts(char_set[index], char_set, common_char_set)
    plains = []
    for s in shifts:
        plains.append(get_plain_text(s, cipher_text, char_set))
    return plains


def calc_score(plain_text):
    plain_text = plain_text.upper()
    my_file = open('common_3000_words.txt', 'r')
    score = 0
    for word in iter(my_file):
        word = word.upper()
        word = word.replace('\n', '')
        if plain_text.find(word) != -1:
            score += 1
    my_file.close()
    return score


def decrypt(cipher_text, char_set, common_char_set):
    scores = []
    temp_scores = []
    plain_texts = find_permutations(cipher_text, char_set, common_char_set)
    for pt in plain_texts:
        temp_scores.append(calc_score(pt))
    outputs = []
    for i in range(len(plain_texts)):
        index = get_max_index(temp_scores)
        if index != -1:
            outputs.append(plain_texts[index])
            scores.append(temp_scores[index])
            temp_scores[index] = 0
    return outputs, scores


def main():
    global character_set, common_character_set
    # read in the encrypted text
    cipher_text = "2XQM5QN7A10QYUXXU104M0P59146T1R5TM4Q5M0PNQOM4QR7X01661NQ5QQ0NA6TQM7564MXUM0S18Q40YQ06M0P2XQM5QNQ8USUXM06"
    # read in the character set
    try:
        print("\033[1;36mAttempting to decrypt...\033[0;0m")
        answers, scores = decrypt(cipher_text, character_set, common_character_set)
        print("Decrypted texts from most confident to the least confident:")
        my_file = open('caesar_is_dead.txt', 'w+')
        output_str = ""
        for i in range(len(answers)):
            print("\033[0;32mScore of most common english words\033[0;0m: %i" % scores[i])
            print("\033[0;32mDecrypted text\033[0;0m: %s" % answers[i])
            output_str += "Score of most common english words: " + str(scores[i]) + "\n"
            output_str += "Decrypted text: " + str(answers[i]) + "\n"
        print("\033[1;36mWriting to file: caesar_is_dead.txt\033[0;0m")
        my_file.write(output_str)
        my_file.close()
        print("\033[1;36mComplete\033[0;0m")
    except EnvironmentError:
        print("\033[1;31mShucks, failed to decrypt this message... I guess Caesar still lives.\033[0;0m ")

if __name__ == '__main__':
    main()
