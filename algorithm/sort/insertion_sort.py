# at the step i, the left side of array [0:i] is sorted
# we take the i-th element, and add it to the right place of the left side of array
# selection_sort: loop for all elements in the right side of array
# insertion_sort: loop for elements in the left side of array
def insertion_sort(collection):

    for i in range(1, len(collection)):
        current = collection[i]
        j = i - 1

        # find the right place in the left-side array to put i-th element
        while j >= 0 and current < collection[j]:
            # shift element to the right to make a hole
            collection[j + 1] = collection[j]
            j = j - 1

        collection[j+1] = current


if __name__ == "__main__":
    input = [1, 3, 2, 7, 8, -5, -3, -2, 10, 4, 100, -9, -8, -10]
    output = insertion_sort(input)

    print(input)
