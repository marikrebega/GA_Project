import random

import ext_value


def get_key(val, dict):
    for key, value in dict.items():
        if val == value:
            return key

    return "key doesn't exist"


def roulette(target, gen):
    if not target:
        min = ext_value.min_val(gen)
        fit_res = {}
        res = []
        for i in range(len(gen)):
            fit_res[i] = ext_value.my_func(gen[i]) / min
        fit_res_sort = sorted(fit_res.values(), reverse=True)
        length = int(len(gen)/2)
        for j in range(length):
            choise = random.uniform(fit_res_sort[len(fit_res_sort)-1], 1.0)
            for i in range(len(gen)):
                if i == len(gen) - 1:
                    if choise <= fit_res_sort[i] and choise >= fit_res_sort[len(fit_res_sort)-1]:
                        key = get_key(fit_res_sort[i], fit_res)
                        res.append(gen[key])
                else:
                    if choise <= fit_res_sort[i] and choise >= fit_res_sort[i + 1]:
                        key = get_key(fit_res_sort[i],fit_res)
                        res.append(gen[key])
        return res


def tournament(target, gen):
    if not target:
        min = ext_value.min_val(gen)
        fit_res = {}
        res = []
        for i in range(len(gen)):
            fit_res[i] = ext_value.my_func(gen[i]) / min
        for i in range(0, len(gen)-1, 2):
            if fit_res[i] >= fit_res[i+1]:
                res.append(gen[i])
            else:
                res.append(gen[i+1])
        return res