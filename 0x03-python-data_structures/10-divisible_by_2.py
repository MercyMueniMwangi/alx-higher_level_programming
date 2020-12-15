#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    divisibles = []
    for n in range(len(my_list)):
        if my_list[n] % 2 == 0:
            divisibles.append(True)
        else:
            divisibles.append(False)

    return (divisibles)
