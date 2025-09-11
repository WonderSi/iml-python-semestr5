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


def num_five():
    array = np.random.randint(1, 101, size=(3, 3, 3))

    print(array)

    return


def num_six():
    array = np.arange(30, 42).reshape(3, 4)

    print(array)

    return


def num_seven():
    array = np.ones((10, 10), dtype=int)
    array[1:-1, 1:-1] = 0

    print(array)

    return


def num_eight():
    array = np.zeros((5, 5), dtype=int)
    np.fill_diagonal(array, np.arange(1, 6))

    print(array)

    return


def num_nine():
    array = np.zeros((4, 4), dtype=int)

    for i in range(4):
        for j in range(4):
            if (i+j) % 2 == 1:
                array[i, j] = 1

    print(array)

    return

if __name__ == "__main__":
    num_one()
    num_two()
    num_three()
    num_four()
    num_five()
    num_six()
    num_seven()
    num_eight()
    num_nine()
