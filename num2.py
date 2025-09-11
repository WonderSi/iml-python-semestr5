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

    print("Уникальные элементы:", unique_elements)
    print("Частоты:", frequencies) 

    return


def num_four():
    array = np.array([1, 2, 3, 4])

    for n in range(1, 4):
        repeated = np.tile(array, n)
        print(f"{n} повторение(я/й):", repeated)
    
    return


def num_five():
    array1 = np.array([200., 300., np.nan, np.nan, np.nan, 700.])
    array_clean1 = array1[~np.isnan(array1)]

    array2 = np.array([[1., 2., 3.],
                [np.nan, 0., np.nan],
                [6., 7., np.nan]])
    array_clean2 = array2[~np.isnan(array2)]

    print(array_clean1)
    print(array_clean2)

    return


def num_six():
    array = np.array([1., 7., 8., 2., 0.1, 3., 15., 2.5])
    k = 4

    index = np.argpartition(array, k)[:k]
    smallest_el = np.sort(array[index])
    print(smallest_el)

    return


def num_seven():
    array = np.array([0.5, 1.8, 2.1, 3.5, 4.87, 5.13, 6.49])
    value = 3.09066280756759

    index = np.argmin(np.abs(array - value))
    closest_value = array[index]

    print(closest_value)

    return


def num_eight():
    array1 = np.array(['Python', 'PHP'])
    array2 = np.array(['Java', 'C++'])

    result = np.char.add(array1, ' ')
    result = np.char.add(result, array2)

    print(result) 


if __name__ == "__main__":
    num_one()
    num_two()
    num_three()
    num_four()
    num_five()
    num_six()
    num_seven()
    num_eight()
