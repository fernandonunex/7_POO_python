from errno import ELIBBAD
import random

def binary_search(array, start, end, target, counter):

    print(f'Searching {target} between {array[start]} and {array[end - 1]} ')

    if start > end:
        return False
    
    medio = (start + end) // 2
    counter += 1

    if array[medio] == target:
        print(f'Steps: {counter}')
        return True
    elif array[medio] < target:
        return binary_search(array, medio + 1, end, target, counter)
    else:
        return binary_search(array, start, medio - 1, target, counter)



if __name__ == '__main__':
    size_of_array = int(input('Size of the array: '))
    target = int(input('What number do you want to find: '))

    array = sorted([random.randint(0, 100) for i in range(size_of_array)])
    found = binary_search(array, 0, len(array), target, 0)

    print(array)
    print(f'\nThe target {target} {"is" if found else "is not"} in the list')