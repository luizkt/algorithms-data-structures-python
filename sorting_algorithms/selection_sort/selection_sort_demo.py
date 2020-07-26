from random import randint


def selection_sort(array):
    for outer_index in range(len(array) - 1):
        for inner_index in range(outer_index, len(array)):
            if array[outer_index] > array[inner_index]:
                array[outer_index], array[inner_index] = array[inner_index], array[outer_index]


min_value = 0
max_value = 20
list_length = 10

test_array = [randint(min_value, max_value) for i in range(list_length)]
print(f"Original list: \n{test_array}")
selection_sort(test_array)
print(f"Sorted list: \n{test_array}")
