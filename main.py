import random

func_f = input("input a factored function: ")
func_g = input("input an expanded function: ")
d = int(input("input a range d, where the range is [1, d]: "))
m = int(input("input the number of random numbers: "))
rand_list = []


def equality_test(func_f, func_g, d, m):
    func_f = func_f.replace(")(", ")*(")  # Move outside the loop
    func_g = ("+" + func_g).replace("x", "*x").replace("+*", "+")  # Move outside the loop
    func_f = func_f.replace("x", "(x)")
    func_g = func_g.replace("x", "(x)")
    func_f = func_f.replace("^", "**")
    func_g = func_g.replace("^", "**")

    for i in range(m):
        random_number = random.randint(1, d)
        print(random_number)
        rand_list.append(random_number)

        modified_func_f = func_f.replace("x", str(random_number))
        modified_func_g = func_g.replace("x", str(random_number))

        print(modified_func_f, modified_func_g)

        if eval(modified_func_f) == eval(modified_func_g):
            print("Yes")
            exit()
        else:
            print("No")
            exit()


equality_test(func_f, func_g, d, m)
