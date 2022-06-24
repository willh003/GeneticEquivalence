import random

def positive_or_negative():
    if random.random() < 0.5:
        return 1
    else:
        return -1