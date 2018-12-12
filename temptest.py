def CutWatermelon(n, k):
    """
    Imagine a watermelon in high-dimensional space
    :param n: int, space dimensions
    :param k: int, cuts
    :return: int, max number of pieces
    """
    if n == 1:
        return k + 1
    elif k == 1:
        return 2

    return CutWatermelon(n, k-1) + CutWatermelon(n-1, k-1)


for i in range(1, 5):
    print(CutWatermelon(4, i))