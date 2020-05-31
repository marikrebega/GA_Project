import random


def one_point_cross(father):
    cross_point = random.randrange(1, 6)
    binary_pop = {}
    new_gen = []
    temp = []
    for i in range(len(father)):
        binary_pop[i] = bin(father[i])
    for i in range(0, len(binary_pop), 2):
        child1 = ""
        child2 = ""
        if binary_pop[i][0:1] == "-" and binary_pop[i + 1][0:1] == "-":
            dad = binary_pop[i][3:].zfill(6)
            mom = binary_pop[i + 1][3:].zfill(6)
            for i in range(cross_point):
                child1 += mom[i]
                child2 += dad[i]
            for i in range(cross_point, len(dad)):
                child1 += dad[i]
                child2 += mom[i]
            dad = "-0b" + dad
            mom = "-0b" + mom
            child1 = "-0b" + child1
            child2 = "-0b" + child2
            temp.append(dad)
            temp.append(mom)
            temp.append(child1)
            temp.append(child2)
            print("mom: ", mom, "dad: ", dad, "\tchild1: ", child1, "child2: ", child2)
        elif binary_pop[i][0:1] == "-" and binary_pop[i + 1][0:1] != "-":
            dad = binary_pop[i][3:].zfill(6)
            mom = binary_pop[i + 1][2:].zfill(6)
            for i in range(cross_point):
                child1 += mom[i]
                child2 += dad[i]
            for i in range(cross_point, len(dad)):
                child1 += dad[i]
                child2 += mom[i]
            dad = "-0b" + dad
            mom = "0b" + mom
            child1 = "0b" + child1
            child2 = "-0b" + child2
            temp.append(dad)
            temp.append(mom)
            temp.append(child1)
            temp.append(child2)
            print("mom: ", mom, "dad: ", dad, "\tchild1: ", child1, "child2: ", child2)
        elif binary_pop[i][0:1] != "-" and binary_pop[i + 1][0:1] == "-":
            dad = binary_pop[i][2:].zfill(6)
            mom = binary_pop[i + 1][3:].zfill(6)
            for i in range(cross_point):
                child1 += mom[i]
                child2 += dad[i]
            for i in range(cross_point, len(dad)):
                child1 += dad[i]
                child2 += mom[i]
            dad = "0b" + dad
            mom = "-0b" + mom
            child1 = "-0b" + child1
            child2 = "0b" + child2
            temp.append(dad)
            temp.append(mom)
            temp.append(child1)
            temp.append(child2)
            print("mom: ", mom, "dad: ", dad, "\tchild1: ", child1, "child2: ", child2)
        else:
            dad = binary_pop[i][2:].zfill(6)
            mom = binary_pop[i + 1][2:].zfill(6)
            for i in range(cross_point):
                child1 += mom[i]
                child2 += dad[i]
            for i in range(cross_point, len(dad)):
                child1 += dad[i]
                child2 += mom[i]
            dad = "0b" + dad
            mom = "0b" + mom
            child1 = "0b" + child1
            child2 = "0b" + child2
            temp.append(dad)
            temp.append(mom)
            temp.append(child1)
            temp.append(child2)
            print("mom: ", mom, "dad: ", dad, "\tchild1: ", child1, "child2: ", child2)
    for i in range(len(temp)):
        new_gen.append(int(temp[i], 2))
    return new_gen
