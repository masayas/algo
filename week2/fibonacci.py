# Uses python3
def calc_fib_naive(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


def calc_fib(n):

    l = [0, 1]
    for i in range(2, n+1):
        l.append(l[-1] + l[-2])
    return l[n]


def stress_test(n):
    """
    Compare the results by _naive and _fast and if there is discrepancy,
    stop the test
    :param int n: number to determine which nth fibonacci we want
    :return:
    """
    while True:
        res1 = calc_fib_naive(n)
        res2 = calc_fib(n)
        if res1 == res2:
            print("ok")
        else:
            print("wrong answer", res1, res2)
            return


if __name__ == "__main__":
    n = int(input())
    print(calc_fib(n))
