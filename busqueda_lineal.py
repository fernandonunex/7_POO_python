import random


def linear_search(array, target):  # Es un O(n)
    match = False

    for element in array:
        if element == target:
            match = True
            break
    return match


if __name__ == '__main__':
    size_of_array = int(input('Size of the array: '))
    target = int(input('What number do you want to find'))

    array = [random.randint(0, 100) for i in range(size_of_array)]
    found = linear_search(array, target)

    print(array)
    print(f'The target {target} {"is" if found else "is not"} in the list')
