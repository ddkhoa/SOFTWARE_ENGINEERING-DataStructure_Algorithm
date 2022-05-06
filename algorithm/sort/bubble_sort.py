# in bubble sort, we try to makes small elements float to the top (the left side of array)
# we use 2 indexes to iterate through the collection and compare adjacent elements
# for each i, the biggest element will be push on the bottom (the right side of array)

def bubble_sort(collection):

    for i in range(len(collection)):

        # for each iteration, if no swap was made, that means the collection is sorted, we can stop the algo
        swapped = False

        # at the i-th iteration, there will be i elements sorted on the right side
        for j in range(len(collection) -1 - i):

            if collection[j] > collection[j+1]:
                collection[j], collection[j+1] = collection[j+1], collection[j]
                swapped = True

        if swapped is False:
            break

    return collection

if __name__ == "__main__":
    input = [1,3,2,7,8,-5,-3,-2,10,4,100,-9,-8,-10]
    output = bubble_sort(input)

    print(input)