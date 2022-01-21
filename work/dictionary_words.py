import random
words = []
rand_words = []

# opens dictionary words
file = open('/usr/share/dict/words', 'r')

# removes new line from words
for line in file:
    words.append(line.rstrip() + " ")

# asks users for number of words
words_requested = input("Enter number of words: ")

# chooses random words
for i in range(int(words_requested)):
    rand_words.append(random.choice(words))

# adds space between words and adds a period at the end
sentence = ' '.join(rand_words) + "."

# prints sentence
print(f"Your sentence is: {sentence}")

file.close()