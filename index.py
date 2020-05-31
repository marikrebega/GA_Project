import crossing
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
        print("Initial popultion: ", gen)
        res = ext_value.min_val(gen)
        print("The MINIMUM value of function = " + str(res))

        for i in range(50):
            new_gen = crossing.one_point_cross(selection.tournament(target, gen))
            print(new_gen)

            gen = new_gen
            res = ext_value.min_val(gen)
            print("The MINIMUM value of function = ", res, "\n")

main()
