# choose a pivot element (middle element in the implement below)
# make sure that:
# all elements on the left are < the pivot
# all elements on the right are > the pivot
# recursive on the left part and the right part
# when the array contains <= 1 element, it is sorted

def quick_sort(collection, left, right):

    if left >= right:
        return

    middle = (left + right)//2
    i = left
    j = right

    while i < j:
        while collection[i] < collection[middle]: # element is in the right place, ignore
            i = i + 1

        while collection[j] > collection[middle]: # same
            j = j - 1

        # swap
        if i < j:
            collection[i], collection[j] = collection[j], collection[i]
            i = i + 1
            j = j - 1

    # recursive for left part [0, i] and right part [i + 1, right]
    quick_sort(collection, 0, i)
    quick_sort(collection, i + 1, right)

    return collection

if __name__ == "__main__":
    input = [1, 3, 2, 7, 8, -5, -3, -2, 10, 4, 100, -9, -8, -10]
    output = quick_sort(input, 0, len(input) - 1)

    print(output)
