import random


def insertion_sort(array):

    for index in range(1, len(array)):
        actual_value = array[index]
        actual_position = index

        while actual_position > 0 and array[actual_position - 1] > actual_value:
            array[actual_position] = array[actual_position - 1]
            actual_position -= 1

        array[actual_position] = actual_value
        print(array)

    return array


if __name__ == '__main__':
    print('Insertion Sort Algorithm')
    size_of_array = int(input('Size of the array: '))

    array = [random.randint(0, 100) for i in range(size_of_array)]
    print("Array random\n")
    print(array)

    sorted_array = insertion_sort(array)

    print("Array sorted\n")
    print(array)
