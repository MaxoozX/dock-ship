import time
import json
import sys

filename = "words.txt"
dest_filename = "words-graph.txt"

alphabet = "abcdefghijklmnopqrstuvwxyz"

with open(filename, "r") as file:
    words = file.read().split()

nb_words = len(words)

print(f"Parsing this list of {nb_words} words.")

set_words = set(words)

adjancency_list = {}

def add_dico(word, test_word):
    global adjancency_list
    if word not in adjancency_list.keys():
        adjancency_list[word] = []
    adjancency_list[word].append(test_word)

t = time.time()

progress_bar_width = 20

last_updated = 0
computed_words = 0

sys.stdout.flush()

sys.stdout.write("Progress : [%s]" % (" " * progress_bar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (progress_bar_width+1)) # return to start of line, after '['

for word in words:
    # We try to change everyletter
    for i in range(len(word)):
        for c in alphabet:
            if c == word[i]: continue
            test_word = word[:i] + c + word[i+1:]
            if test_word in set_words:
                add_dico(word, test_word)
    computed_words += 1
    if (computed_words - last_updated) > (nb_words // progress_bar_width):
        sys.stdout.write("-")
        sys.stdout.flush()
        last_updated = computed_words

print(f"Done in {round(time.time() - t, 2)} seconds.")

print("Writing the words in a file")

with open(dest_filename, "w") as file:
    json.dump(adjancency_list, file)

print("Everything is ready, the program is set up.")