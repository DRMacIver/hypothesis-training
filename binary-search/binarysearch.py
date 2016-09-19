def binary_search(ls, value):
    """If ls is sorted, return the smallest index i such that
    ls.insert(i, value) would still be sorted.

    If ls is not sorted, the result from this function may be any value i in
    the range 0 <= i <= len(ls)

    """
    if not ls:
        return 0
    if value > ls[-1]:
        return len(ls)
    if value <= ls[0]:
        return 0
    lo = 0
    hi = len(ls) - 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        pivot = ls[mid]
        if value < pivot:
            hi = mid
        elif pivot == value:
            return mid
        else:
            lo = mid
    assert ls[lo] < value
    assert ls[hi] >= value
    return hi
