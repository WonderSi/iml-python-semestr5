import numpy as np


def num_one():
    arr1 = np.array([0, 10, 20, 40, 60])
    arr2 = np.array([10, 30, 40])
    common_elements = np.intersect1d(arr1, arr2)

    print(common_elements)
    
    return


def num_two():
    arr1 = np.array([10, 10, 20, 20, 30, 30])
    unique_elements1 = np.unique(arr1)

    arr2 = np.array([[1, 1], [2, 3]])
    unique_elements2 = np.unique(arr2)

    print(unique_elements1)
    print(unique_elements2)


if __name__ == "__main__":
    num_one()
    num_two()
