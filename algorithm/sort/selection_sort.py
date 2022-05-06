def selection_sort(collection):

    # use 2 index to iterate over the collection
    # first index i go from 0 -> len - 1
    # second index j go from i + 1 -> len
    # the second index j is used to find the minimum value and swap to element at i
    # so, for each i, we put the minimum value in the right place

    length = len(collection)
    for i in range(length - 1):

        # find the index of minimum value
        min_index = i

        for j in range(i+1, length):
            if collection[min_index] > collection[j]:
                min_index = j

        # swap
        if i != min_index:
            collection[i], collection[min_index] = collection[min_index], collection[i]

    return collection

if __name__ == "__main__":
    input = [1,3,2,7,8,-5,-3,-2,10,4,100,-9,-8,-10]
    output = selection_sort(input)

    print(input)