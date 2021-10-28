#!/usr/bin/env python
# -*- coding: utf-8 -*-

DATA_IMPUT = [
    ['123','premium','karnivora','pequeña','17.000'],
    ['124','especial','colombiana1','pequeña','15.900'],
    ['125', 'especial', 'colombiana2', 'pequeña', '15.900'],
    ['126', 'especial', 'colombiana3', 'pequeña', '15.900'],

    ['321','tradicional','carnes','mediana','27.500'],
    ['322','no tradicional','carnes 2.0','mediana','30.500'],
    ['323', 'super tradicional', 'carnes 3.0', 'mediana', '40.500'],
]


def get_max_value(value_1, value_2):
    """
    compare value and return the max value
    params value_1 Int value 1 Ie, 2000
    params value_2 Int value 2 Ie, 2500
    return int, max value Ie 2500
    """

    if value_1 > value_2:
        return value_1
    return value_2


def generate_combinatory():
    for row in DATA_IMPUT:
        for row2 in DATA_IMPUT[::-1]:
            if row[0] == row2[0]:
                break
            if (not row[0] == row2[0]) and row[3] == row2[3]:
                print('combinacion: 1/2 {} y 1/2 {}, tamaño: {}, por un valor de: {}'.format(
                    row[2], row2[2], row[3], get_max_value(row[4], row2[4])
                ))


def run_code():
    print('')
    print('--- init ---')
    generate_combinatory()
    print()
    print('--- end ---')


if __name__ == "__main__":
    run_code()
