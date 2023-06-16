import random

func_f = input("input a functon:")
func_g = input("input a functon:")
d = int(input("input a range d, where the range is [1, d]:"))
m = int(input("input the number of random numbers: "))
rand_list = []


def equality_test(func_f, func_g, d, m):
    for i in range(m):
        x = random.randint(1, d)
        rand_list.append(x)
        func_f = func_f.replace(")(", ")*(")
        func_g = func_g.replace("")
        print(func_f, func_g)
        func_f = func_f.replace("x", "(x)")
        func_g = func_g.replace("x", "(x)")
        print(func_f, func_g)
        func_f = func_f.replace("x", str(m))
        func_g = func_g.replace("x", str(m))
        print(func_f, func_g)
        func_f = func_f.replace("^", "**")
        func_g = func_g.replace("^", "**")
        print(func_f, func_g)
        if eval(func_f) == eval(func_g):
            print("Yes")


equality_test(func_f, func_g, d, m)
