# max_pairwise_product
# https://courses.edx.org/courses/course-v1:UCSanDiegoX+ALGS200x+2T2017/pdfbook/0/
from random import randint


def max_pairwise_product_naive(max_length, numbers):
    """
    find two highest numbers and return their product
    from the given list
    :param int max_length:
    :param list numbers:
    :return:
    """
    result = 0
    for i in range(0, max_length):
        for j in range(i+1, max_length):
            if numbers[i]*numbers[j] > result:
                result = numbers[i]*numbers[j]
    return result


def max_pairwise_product_fast(max_length, numbers):
    """
    find two highest numbers and return their product
    from the given list
    :param int max_length:
    :param list numbers:
    :return:
    """
    max_index1 = 0
    for i in range(1, max_length):
        if numbers[i] > numbers[max_index1]:
            max_index1 = i
    if max_index1 == 0:
        max_index2 = 1
    else:
        max_index2 = 0
    for i in range(max_length):
        if i != max_index1 and numbers[i] > numbers[max_index2]:
            max_index2 = i
    return numbers[max_index1] * numbers[max_index2]


def stress_test(max_length, max_random_num):
    """
    Compare the results by _naive and _fast and if there is discrepancy,
    stop the test
    :param int max_length:
    :param int max_random_num:
    :return:
    """
    while True:
        n = randint(2, max_length)
        a = [randint(2, max_random_num) for i in range(n)]
        print(a)
        res1 = max_pairwise_product_naive(n, a)
        res2 = max_pairwise_product_fast(n, a)
        if res1 == res2:
            print("ok")
        else:
            print("wrong answer", res1, res2)
            return


if __name__ == '__main__':
    max_len = int(input())
    a = [int(x) for x in input().split()]
    assert (len(a) == max_len)

    print(max_pairwise_product_fast(max_len, a))

