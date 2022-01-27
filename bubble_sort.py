import random


def bubble_sort(array):
    n = len(array)

    for i in range(n):
        for j in range(0, n - i - 1):  # O(n) * O(n - i -1) = O(n*n) = O(n^2)
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


if __name__ == '__main__':
    print('Bubble Sort')
    size_of_array = int(input('Size of the array: '))

    array = [random.randint(0, 100) for i in range(size_of_array)]
    print("Array random\n")
    print(array)

    sorted_array = bubble_sort(array)

    print("Array sorted\n")
    print(array)
