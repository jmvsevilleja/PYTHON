import random
print("# RANDOM STRING without Repetition")

name = "Jess"
result = random.sample(name, k=len(name))
print("".join(result))

print("# RANDOM WORDS using SET")


def get_unique_words(all_words):
    words = set()
    for _ in range(1000):
        words.add(random.choice(all_words))
    return words


all_words = "all the words in the world".split()
print(get_unique_words(all_words))
