import random


def shuffleString(text):
    list_string = list(text)
    random.sample(list_string)
    return "".join(list_string)


print(shuffleString("TheQuickBrownFox"))
