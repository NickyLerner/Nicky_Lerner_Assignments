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

print("---LINEAR SEARCH---")

alice_full_text_by_words = []

'''for line in range(len(alice_full_text_by_line)):
    # print(line, alice_full_text_by_line[line])
    alice_current_line_by_words = split_line(alice_full_text_by_line[line])
    for words in alice_current_line_by_words:
        if words.upper() not in dictionary:
            print("In line", str(line + 1) + ", possible word,", words + ", misspelled.")'''

print("---BINARY SEARCH---")

