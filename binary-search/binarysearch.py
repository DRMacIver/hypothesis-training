def binary_search(list, value):
    """If list is sorted, return the smallest index i such that
    ls.insert(value) would still be sorted.

    If list is not sorted, the result from this function may be any value i in
    the range 0 <= i <= len(list)

    """
    if not list:
        return 0
    if value > list[-1]:
        return len(list)
    if value <= list[0]:
        return 0
    lo = 0
    hi = len(list) - 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        pivot = list[mid]
        if value < pivot:
            hi = mid
        elif pivot == value:
            return mid
        else:
            lo = mid
    assert list[lo] < value
    assert list[hi] >= value
    return hi
