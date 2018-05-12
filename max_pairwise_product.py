# Uses python3


def max_pairwise_product_fast(n, numbers):
    max_index1 = 0
    for i in range(1, n):
        if numbers[i] > numbers[max_index1]:
            max_index1 = i
    if max_index1 == 0:
        max_index2 = 1
    else:
        max_index2 = 0
    for i in range(n):
        if i != max_index1 and numbers[i] > numbers[max_index2]:
            max_index2 = i
    return numbers[max_index1] * numbers[max_index2]


if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
    assert (len(a) == n)

    print(max_pairwise_product_fast(n, a))
