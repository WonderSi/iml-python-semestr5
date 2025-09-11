import numpy as np


def num_one():
    array1 = np.array([0, 10, 20, 40, 60])
    array2 = np.array([10, 30, 40])
    common_elements = np.intersect1d(array1, array2)

    print(common_elements)
    
    return


def num_two():
    array1 = np.array([10, 10, 20, 20, 30, 30])
    unique_elements1 = np.unique(array1)

    array2 = np.array([[1, 1], [2, 3]])
    unique_elements2 = np.unique(array2)

    print(unique_elements1)
    print(unique_elements2)

    return


def num_three():
    array = np.array([10, 10, 20, 10, 20, 20, 20, 30, 30, 50, 40, 40])

    unique_elements, frequencies = np.unique(array, return_counts=True)

    print("Unique elements:", unique_elements)
    print("Frequencies:", frequencies) 

    return


if __name__ == "__main__":
    num_one()
    num_two()
    num_three()
