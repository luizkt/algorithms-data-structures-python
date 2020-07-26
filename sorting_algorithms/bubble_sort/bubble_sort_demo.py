from random import randint


def bubble_sort(array):
    swap = True
    while swap:
        swap = False
        for index in range(len(array) - 1):
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]
                swap = True


min_value = 0
max_value = 20
list_length = 10

test_array = [randint(min_value, max_value) for i in range(list_length)]
print(f"Original list: \n{test_array}")
bubble_sort(test_array)
print(f"Sorted list: \n{test_array}")
