def subsets(A):
    n = len(A)
    res = []

    for i in range(1 << n):
        res.append([])
        for j in range(n):
            if (i & (1 << j)) != 0:
                res[i].append(A[j])
    return res


def zero_sum(A):
    res = []

    for subset in subsets(A):
        sum = 0
        for i in subset:
            sum += i
        if sum == 0 and len(subset) > 0:
            res.append(subset)
    return res


if __name__ == "__main__":
    array = [1, 2, 3, -2]
    res = zero_sum(array)
    print(res)
