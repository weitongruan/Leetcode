from random import randint
def partition(list, left, right, pivotIndex):
    pivotValue = list[pivotIndex]
    list[right], list[pivotIndex] = pivotValue, list[right]
    storeIndex = left
    for i in xrange(left, right):
        if list[i] < pivotValue:
            list[storeIndex], list[i] = list[i], list[storeIndex]
            storeIndex += 1
    list[storeIndex], list[right] = pivotValue, list[storeIndex]
    return storeIndex

def select(list, left, right, n):
    if left == right:
        return list[left]
    pivotIndex = randint(left, right)
    pivotIndex = partition(list, left, right, pivotIndex)

    if n == pivotIndex + 1:
        return list[n]
    elif n < pivotIndex + 1:
        return select(list, left, pivotIndex - 1, n)
    else:
        return select(list, pivotIndex + 1, right, n)

def select_linearMemory(list, left, right, n):
    while True:
        if left == right:
            return list[left]
        pivotIndex = randint(left, right)
        pivotIndex = partition(list, left, right, pivotIndex)
        if n == pivotIndex + 1:
            return list[n]
        elif n < pivotIndex + 1:
            right = pivotIndex - 1
        else:
            left = pivotIndex + 1

def main():

    array = [5, 1, 2, 4, 15, 3, 6, 11, 8, 7, 2, 15, 7]
    # array = [6, 5, 4, 3, 2, 1]
    print select_linearMemory(array, 0, len(array)-1, 6)
    print array
    print sorted(array)


main()