# Read sentences from file "Building_Global_Community.txt"
lines = []
for line in open('building_global_community.txt'):
    line = line.strip()
    lines.append(line)

print(lines)

# Filter out symbols and normalize words
words = []
for line in lines:
    wordlist = line.split(" ")

    for word in wordlist:
        word = word.strip('?!:,. "-')
        word = word.lower()
        if word != "":
            words.append(word)

print(words)

# Count the occurance of words - way 1
counter = {}
for word in words:
    if word in counter:
        counter[word] += 1
    else:
        counter[word] = 1

print(counter)

# Count the occurance of words- way 2 
from collections import Counter
wordCounter = Counter(words)
wordCounter

print(wordCounter.most_common(20))