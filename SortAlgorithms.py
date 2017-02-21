import heapq

def InsertionSort(A):
    for i in xrange(len(A)):
        j = i - 1
        while j >= 0 and A[j] > A[j+1]:
            A[j], A[j + 1] = A[j + 1], A[j]
            j -= 1
    return A


def MergeSort(A):
    if len(A) == 1:
        return A

    l, r = MergeSort(A[: len(A) / 2]), MergeSort(A[len(A) / 2:])

    result = []

    while len(l) and len(r):
        result.append(l.pop(0) if l[0] <= r[0] else r.pop[0])

    return result + l if len(l) else result + r


def QuickSort(A, start, end):
    if start < end:
        p = partition(A, start, end)
        QuickSort(A, start, p - 1)
        QuickSort(A, p + 1, end)
    return A


def partition(A, start, end):
    pivot = A[start]
    left = start + 1
    right = end
    done = False

    while not done:
        while left <= right and A[left] <= pivot:
            left += 1
        while right >= left and A[right] >= pivot:
            right -= 1
        if right < left:
            done = True
        else:
            A[left], A[right] = A[right], A[left]

    A[start], A[right] = A[right], A[start]
    return right

def HeapSort(A):
    heapq.heapify(A)
    return A

def CountingSort(A, k):
    count = [0] * (k + 1)
    for num in A:
        count[num] += 1

    idx = 0
    for i in xrange(len(count)):
        while count[i] > 0:
            count[i] -= 1
            A[idx] = i
            idx += 1
    return A

def StableCountingSort(A, k):
    output = [0]* (len(A))
    count = [0] * (k+1)
    for num in A:
        count[num] += 1
    for i in xrange(1, k+1):
        count[i] += count[i-1]
    for i in range(len(A))[::-1]:
        output[count[A[i]]-1] = A[i]
        count[A[i]] -= 1
    return output

def main():

    array = [5, 1, 2, 4, 15, 3, 6, 11, 8, 7, 2, 15, 7]

    print array
    print InsertionSort(array)
    print MergeSort(array)
    print QuickSort(array, 0, len(array)-1)
    print HeapSort(array)
    print CountingSort(array, 16)
    print StableCountingSort(array, 16)


main()