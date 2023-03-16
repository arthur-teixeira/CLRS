def partition(A, p, r):
    pivot = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            A[j], A[i] = A[i], A[j]

    i += 1
    A[i], A[r] = A[r], A[i]
    return i

def tail_recursive_qsort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        if q < (p + r) // 2:
            tail_recursive_qsort(A, p, q - 1)
            p = q + 1
        else:
            tail_recursive_qsort(A, q + 1, r)
            r = q - 1


if __name__ == "__main__":
    A = [4, 9345, 9238, 348, 74, 93, 859, 1, 2, 670]
    tail_recursive_qsort(A, 0, len(A) - 1)
    print(A)
