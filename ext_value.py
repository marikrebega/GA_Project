def min_val(gen):
    min_value = my_func(gen[0])
    for i in range(len(gen)):
        value = my_func(gen[i])
        if min_value > value:
            min_value = value
    return min_value


def max_val(gen):
    max_value = my_func(gen[0])
    for i in range(len(gen)):
        value = my_func(gen[i])
        if max_value < value:
            max_value = value
    return max_value


def my_func(person):
    a = 14
    b = 2
    c = -26
    d = 1
    value = a + (b * person) + (c * person ^ 2) + (d * person ^ 3)
    return value
