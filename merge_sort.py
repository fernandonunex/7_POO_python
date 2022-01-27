import random


def merge_sort(array):
    if len(array) > 1:
        medium = len(array) // 2
        left = array[:medium]
        right = array[medium:]
        print(left, '*' * 5, right)

        #Recusivity in both sides
        merge_sort(left)
        merge_sort(right)

        #Iterators for sub arrays
        i = 0
        j = 0
        #Iterator for main array
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            
            k += 1
        
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(left):
            array[k] = right[j]
            j += 1
            k += 1
        print(f'Left: {left}, right {right}')
        print(array)
        print('-' * 50)

    return array



if __name__ == '__main__':
    print('Merge Sort Algorithm')
    size_of_array = int(input('Size of the array: '))

    array = [random.randint(0, 100) for i in range(size_of_array)]
    print("Array random\n")
    print(array)
    print('-' * 20)

    sorted_array = merge_sort(array)

    print("Array sorted\n")
    print(sorted_array)
