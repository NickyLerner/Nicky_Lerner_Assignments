'''
Complete the chapter lab at http://programarcadegames.com/index.php?chapter=lab_spell_check
'''
import re


# Alice in Wonderland Spell Check

def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


with open('dictionary.txt', 'r') as f:
    dictionary = [x.strip().upper() for x in f]

with open('AliceInWonderland.txt') as f:
    alice_full_text_by_line = [x.strip() for x in f]

with open('AliceInWonderland200.txt') as f:
    alice_chapter_one_by_line = [x.strip() for x in f]

print("---LINEAR SEARCH---")


def linear_search(text):
    i = 0
    good_word = True
    for line in range(len(text)):
        text_current_line_by_words = split_line(text[line])
        for words in text_current_line_by_words:
            while i < len(dictionary) and words.upper() != dictionary[i]:
                i += 1
            if i == len(dictionary):
                good_word = False
            if not good_word:
                print("In line", str(line + 1) + ", possible word,", words + ", misspelled.")
            good_word = True
            i = 0


# linear_search(alice_chapter_one_by_line)

print("---BINARY SEARCH---")


def binary_search(text):
    good_word = True
    for line in range(len(text)):
        text_current_line_by_words = split_line(text[line])
        for words in text_current_line_by_words:
            lower_boundary = 0
            upper_boundary = len(dictionary) - 1
            found = False
            while lower_boundary <= upper_boundary and not found:
                middle_pos = (lower_boundary + upper_boundary) // 2
                # Figure out if we:
                # move up the lower bound, or
                # move down the upper bound, or
                # we found what we are looking for
                if dictionary[middle_pos] < words.upper():
                    lower_boundary = middle_pos + 1
                elif dictionary[middle_pos] > words.upper():
                    upper_boundary = middle_pos - 1
                else:
                    found = True
            if not found:
                print("In line", str(line + 1) + ", possible word,", words + ", misspelled.")


binary_search(alice_chapter_one_by_line)


'''# Loop until we find the item, or our upper/lower bounds meet
for words in alice_full_text_by_line
    '''
