# Angelo Andrade
# 10/6/24
# lists.py
from enum import unique

# List all unique words, sorted in alphabetical order,
# that are stored in a file romeo.txt containing
# a subset of Shakespeare’s work.

fh = open('romeo.txt')

distinct_words = []

for line in fh:
    words = line.split()

    for word in words:
        if word not in distinct_words:
            distinct_words.append(word)

distinct_words.sort()

print(distinct_words)