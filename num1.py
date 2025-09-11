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

if __name__ == "__main__":
    num_one()
