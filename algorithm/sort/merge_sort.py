
def merge(collection, left, middle, right):

    # create left array and right array from the original array
    # don't use slicing here because the index problem (integer division)
    n1 = middle - left + 1
    n2 = right - middle

    left_array = [0] * n1
    right_array = [0] * n2

    for i in range(n1):
        left_array[i] = collection[left + i]
    for i in range(n2):
        right_array[i] = collection[middle + 1 + i]

    i = 0
    j = 0
    k = left

    while i < len(left_array) and j < len(right_array):
        if left_array[i] <= right_array[j]:
            collection[k] = left_array[i]
            i = i + 1
            k = k + 1

        else:
            collection[k] = right_array[j]
            j = j + 1
            k = k + 1

    while i < len(left_array):
        collection[k] = left_array[i]
        i = i + 1
        k = k + 1

    while j < len(right_array):
        collection[k] = right_array[j]
        j = j + 1
        k = k + 1

def merge_sort(collection, left, right):

    if left >= right:
        return

    middle = (left + right) // 2

    merge_sort(collection, left, middle)
    merge_sort(collection, middle + 1, right)
    merge(collection, left, middle, right)

    return collection


if __name__ == "__main__":
    input = [1, 3, 2, 7, 8, -5, -3, -2, 10, 4, 100, -9, -8, -10]
    output = merge_sort(input, 0, len(input) - 1)

    print(output)
