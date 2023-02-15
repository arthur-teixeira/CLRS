def left(i):
    return i*2+1


def right(i):
    return i*2+2


def max_heapify(A, n, i):
    l_index = left(i)
    r_index = right(i)

    if l_index < n and A[l_index] > A[i]:
        largest = l_index
    else:
        largest = i

    if r_index < n and A[r_index] > A[largest]:
        largest = r_index
    if largest != i:
        (A[i], A[largest]) = (A[largest], A[i])
        max_heapify(A, n, largest)


def build_max_heap(A):
    n = len(A)
    for k in range(n//2, -1, -1):
        max_heapify(A, n, k)


def heap_sort(A):
    build_max_heap(A)
    for i in range((len(A)-1), 0, -1):
        (A[i], A[0]) = (A[0], A[i])
        max_heapify(A, i, 0)


if __name__ == "__main__":
    A = [4, 23, 7, 87, 1, 98, 5, 2, 67, 109, 130]
    build_max_heap(A)
    print(A)
    heap_sort(A)
    print(A)
