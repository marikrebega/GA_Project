import random


def make_gen_blanket():
    generations = []
    for i in range(-10, 53, 1):
        generations.append(i)
    return generations


def make_gen_shotgun():
    generations = []
    length = int(len(range(-10, 53, 1))/2)
    for i in range(length):
        generations.append(random.randrange(-10, 53))
    return generations


def make_gen_selective():
    generations = []
    length = 8
    for i in range(length):
        generations.append(random.randrange(-10, 53))
    return generations
