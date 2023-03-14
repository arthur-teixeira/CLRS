def hoare_partition(A, p, r):
    x = A[p]
    i = p - 1
    j = r + 1

    while True:
        while True:
            j -= 1
            if A[j] <= x:
                break

        while True:
            i += 1
            if A[i] >= x:
                break

        if i < j:
            A[i], A[j] = A[j], A[i]
        else:
            return j


def qsort(A, p, r):
    if p < r:
        q = hoare_partition(A, p, r)
        qsort(A, p, q)
        qsort(A, q + 1, r)


if __name__ == "__main__":
    A = [4, 9345, 9238, 348, 74, 93, 859, 1, 2, 670]
    qsort(A, 0, len(A) - 1)
    print(A)
