import ext_value
import population
import selection


def main():
    while True:
        print("Input 0 if you search min value or 1 if you search max value")
        inp = int(input())
        if inp == 0:
            target = False
            print("You search min value\n")
            break
        elif inp == 1:
            target = True
            print("You search max value\n")
            break
        else: print("Wrong argument")

    if not target:
        gen = population.make_gen_selective()
        for i in range(len(gen)):
            print(gen[i])

        res = ext_value.min_val(gen)
        print("min = " + str(res))
        print(selection.tournament(target, gen))


main()
