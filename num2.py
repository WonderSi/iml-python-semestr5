import numpy as np


def num_one():
    arr1 = np.array([0, 10, 20, 40, 60])
    arr2 = np.array([10, 30, 40])
    common_elements = np.intersect1d(arr1, arr2)

    print(common_elements)
    
    return


if __name__ == "__main__":
    num_one()
