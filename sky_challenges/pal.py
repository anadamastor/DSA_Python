# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # Looking for letters appearing in couples
    letter_freq = {}
    for letter in S:
        # creating a frequency vector with the firections
        letter_freq.setdefault(letter, 0)
        letter_freq[letter] += 1
    # return letter_freq

    remaning_letters={}

    for letter, frequency in letter_freq.items():
        if frequency % 2 != 0:
            remaning_letters[letter] = frequency

    if min 
    central_letter = min(remaning_letters, key=remaning_letters.get)
    del remaning_letters[central_letter]

    counter = 0
    for letter, frequency in remaning_letters.items():
        counter += frequency % 2

    return counter

print(solution("aaabab"))