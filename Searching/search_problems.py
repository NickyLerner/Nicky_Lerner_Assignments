import re

'''
Complete the following 3 searching problems using techniques
from class and from Ch15 of the textbook website
'''


def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


# 1.  (6pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.

length = 0
longest_words = []

with open('dictionary.txt', 'r') as f:
    dictionary = [x.strip().upper() for x in f]

for words in dictionary:
    if length <= len(words):
        length = len(words)

for words in dictionary:
    if length <= len(words):
        if words not in longest_words:
            longest_words.append(words)

for words in longest_words:
    print(words)

# 2.  (8pts)  Write code which finds
# The total word count AND average word length
# in "AliceInWonderLand.txt"

with open('AliceInWonderland.txt') as f:
    alice_full_text = [x.strip() for x in f]

alice_words = []

for line in alice_full_text:
    alice_words += split_line(line).upper()

print(alice_words)
alice_word_length = 0

for i in range(len(alice_words)):
    alice_word_length += len(alice_words[i])

alice_word_length = (alice_word_length/len(alice_full_text))

print("WORD COUNT =", len(alice_words))
print("AVG WORD LEN =", alice_word_length)

# CHOOSE ONE OF THE FOLLOWING TWO PROBLEMS

# 3 (12pts)  How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?

#### OR #####

# 3  (12pts)Find the most frequently occurring
# seven letter word in "AliceInWonderLand.txt"

for i in range(2):
    print("OOOOOOO")

# Challenge problem (for fun).
# What words appear in the text of "Alice in Wonderland"
# that DO NOT occur in "Alice Through the Looking Glass".
# Make a list.  You can substitute this for any of the above problems.
