import numpy as np


def num_one():
    array = np.array([1, 7, 13, 105])
    print(array.nbytes)

    np.savetxt("array.txt", array, fmt="%d")
    np.save("array.npy", array)
    array_txt = np.loadtxt("array.txt", dtype=np.int64)
    array_bin = np.load("array.npy")

    print("Loaded from txt - ", array_txt)
    print("Loaded from bin - ", array_bin)

    return


def num_two():
    array_zero = np.zeros(10, dtype=int)
    array_one = np.ones(10, dtype=int)
    array_five = np.full(10, 5, dtype=int)

    print(array_zero)
    print(array_one)
    print(array_five)

    return


def num_three():
    array = np.arange(30, 71, 2)

    print(array)

    return


def num_four():
    array = np.linspace(5, 50, 10, dtype=int)

    print(array)

    return


if __name__ == "__main__":
    num_one()
    num_two()
    num_three()
    num_four()
