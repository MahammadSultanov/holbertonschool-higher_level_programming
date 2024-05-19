#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    from sys import argv, exit
    argc = len(argv)
    if argc == 4:
        a = int(argv[1])
        op = argv[2]
        b = int(argv[3])
        if op == "+":
            res = add(a, b)
        elif op == "-":
            res = sub(a, b)
        elif op == "*":
            res = mul(a, b)
        elif op == "/":
            res = div(a, b)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    print("{} {} {} = {}".format(a, op, b, res))
