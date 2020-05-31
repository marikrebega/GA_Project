import random


def mutate(person):
    position = random.randrange(0, 7)
    temp_person = ""
    for i in range(len(person)):
        if i == position and person[i] == '1':
            temp_person += "".join('0')

        elif i == position and person[i] == '0':
            temp_person += "".join('1')
        else:
            temp_person += "".join(person[i])
    return temp_person


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
            for j in range(cross_point):
                child1 += mom[j]
                child2 += dad[j]
            for j in range(cross_point, len(dad)):
                child1 += dad[j]
                child2 += mom[j]
            if random.randrange(1, 100) == 1:
                person = random.randrange(0, 4)
                if person == 0:
                    dad = mutate(dad)
                elif person == 1:
                    mom = mutate(mom)
                elif person == 2:
                    child1 = mutate(child1)
                elif person == 3:
                    child2 = mutate(child2)
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
            for j in range(cross_point):
                child1 += mom[j]
                child2 += dad[j]
            for j in range(cross_point, len(dad)):
                child1 += dad[j]
                child2 += mom[j]
            if random.randrange(1, 100) == 1:
                person = random.randrange(0, 4)
                if person == 0:
                    dad = mutate(dad)
                elif person == 1:
                    mom = mutate(mom)
                elif person == 2:
                    child1 = mutate(child1)
                elif person == 3:
                    child2 = mutate(child2)
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
            for j in range(cross_point):
                child1 += mom[j]
                child2 += dad[j]
            for j in range(cross_point, len(dad)):
                child1 += dad[j]
                child2 += mom[j]
            if random.randrange(1, 100) == 1:
                person = random.randrange(0, 4)
                if person == 0:
                    dad = mutate(dad)
                elif person == 1:
                    mom = mutate(mom)
                elif person == 2:
                    child1 = mutate(child1)
                elif person == 3:
                    child2 = mutate(child2)
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
            for j in range(cross_point):
                child1 += mom[j]
                child2 += dad[j]
            for j in range(cross_point, len(dad)):
                child1 += dad[j]
                child2 += mom[j]
            if random.randrange(1, 100) == 1:
                person = random.randrange(0, 4)
                if person == 0:
                    dad = mutate(dad)
                elif person == 1:
                    mom = mutate(mom)
                elif person == 2:
                    child1 = mutate(child1)
                elif person == 3:
                    child2 = mutate(child2)
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


def two_point_cross(father):
    tmp_point_1 = random.randrange(1, 6)
    tmp_point_2 = random.randrange(1, 6)
    while tmp_point_1 == tmp_point_2:
        tmp_point_2 = random.randrange(1, 6)
    cross_point = [tmp_point_1, tmp_point_2]
    cross_point.sort()
    print("Cross Point", cross_point)
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
            for j in range(cross_point[0]):
                child1 += mom[j]
                child2 += dad[j]
            for j in range(cross_point[0], cross_point[1]):
                child1 += dad[j]
                child2 += mom[j]
            for j in range(cross_point[1], len(dad)):
                child1 += mom[j]
                child2 += dad[j]
            if random.randrange(1, 100) == 1:
                person = random.randrange(0, 4)
                if person == 0:
                    dad = mutate(dad)
                elif person == 1:
                    mom = mutate(mom)
                elif person == 2:
                    child1 = mutate(child1)
                elif person == 3:
                    child2 = mutate(child2)
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
            for j in range(cross_point[0]):
                child1 += mom[j]
                child2 += dad[j]
            for j in range(cross_point[0], cross_point[1]):
                child1 += dad[j]
                child2 += mom[j]
            for j in range(cross_point[1], len(dad)):
                child1 += mom[j]
                child2 += dad[j]
            if random.randrange(1, 100) == 1:
                person = random.randrange(0, 4)
                if person == 0:
                    dad = mutate(dad)
                elif person == 1:
                    mom = mutate(mom)
                elif person == 2:
                    child1 = mutate(child1)
                elif person == 3:
                    child2 = mutate(child2)
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
            for j in range(cross_point[0]):
                child1 += mom[j]
                child2 += dad[j]
            for j in range(cross_point[0], cross_point[1]):
                child1 += dad[j]
                child2 += mom[j]
            for j in range(cross_point[1], len(dad)):
                child1 += mom[j]
                child2 += dad[j]
            if random.randrange(1, 100) == 1:
                person = random.randrange(0, 4)
                if person == 0:
                    dad = mutate(dad)
                elif person == 1:
                    mom = mutate(mom)
                elif person == 2:
                    child1 = mutate(child1)
                elif person == 3:
                    child2 = mutate(child2)
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
            for j in range(cross_point[0]):
                child1 += mom[j]
                child2 += dad[j]
            for j in range(cross_point[0], cross_point[1]):
                child1 += dad[j]
                child2 += mom[j]
            for j in range(cross_point[1], len(dad)):
                child1 += mom[j]
                child2 += dad[j]
            if random.randrange(1, 100) == 1:
                person = random.randrange(0, 4)
                if person == 0:
                    dad = mutate(dad)
                elif person == 1:
                    mom = mutate(mom)
                elif person == 2:
                    child1 = mutate(child1)
                elif person == 3:
                    child2 = mutate(child2)
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


def mask_cross(father):
    mask = ""
    for i in range(6):
        mask += "".join(str(random.randrange(0, 2)))
    print("Crossing mask", mask)
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
            for j in range(len(mask)):
                if mask[j] == "1":
                    child1 += mom[j]
                    child2 += dad[j]
                elif mask[j] == "0":
                    child1 += dad[j]
                    child2 += mom[j]
            if random.randrange(1, 100) == 1:
                person = random.randrange(0, 4)
                if person == 0:
                    dad = mutate(dad)
                elif person == 1:
                    mom = mutate(mom)
                elif person == 2:
                    child1 = mutate(child1)
                elif person == 3:
                    child2 = mutate(child2)
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
            for j in range(len(mask)):
                if mask[j] == "1":
                    child1 += mom[j]
                    child2 += dad[j]
                elif mask[j] == "0":
                    child1 += dad[j]
                    child2 += mom[j]
            if random.randrange(1, 100) == 1:
                person = random.randrange(0, 4)
                if person == 0:
                    dad = mutate(dad)
                elif person == 1:
                    mom = mutate(mom)
                elif person == 2:
                    child1 = mutate(child1)
                elif person == 3:
                    child2 = mutate(child2)
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
            for j in range(len(mask)):
                if mask[j] == "1":
                    child1 += mom[j]
                    child2 += dad[j]
                elif mask[j] == "0":
                    child1 += dad[j]
                    child2 += mom[j]
            if random.randrange(1, 100) == 1:
                person = random.randrange(0, 4)
                if person == 0:
                    dad = mutate(dad)
                elif person == 1:
                    mom = mutate(mom)
                elif person == 2:
                    child1 = mutate(child1)
                elif person == 3:
                    child2 = mutate(child2)
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
            for j in range(len(mask)):
                if mask[j] == "1":
                    child1 += mom[j]
                    child2 += dad[j]
                elif mask[j] == "0":
                    child1 += dad[j]
                    child2 += mom[j]
            if random.randrange(1, 100) == 1:
                person = random.randrange(0, 4)
                if person == 0:
                    dad = mutate(dad)
                elif person == 1:
                    mom = mutate(mom)
                elif person == 2:
                    child1 = mutate(child1)
                elif person == 3:
                    child2 = mutate(child2)
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
