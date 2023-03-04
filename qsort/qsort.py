def partition(A, p, r):
    pivot = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            A[j], A[i] = A[i], A[j]
    A[i + 1], A[r] = A[r], A[i + 1]

    return i + 1


def qsort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        qsort(A, p, q - 1)
        qsort(A, q + 1, r)


if __name__ == "__main__":
    A = [4, 9345, 9238, 348, 74, 93, 859, 1, 2, 670]
    qsort(A, 0, len(A) - 1)
    print(A)
