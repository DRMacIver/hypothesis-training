"""This module provides a pair of functions for converting lists to and from a
"run length encoding" format, where successive runs of the same value are
represented by that value and a count of how many times in a row it should
appear.

For example, the list [1, 1, 3, 1] in run-length encoded form is
[[2, 1], [1, 3], [1, 1]].

run_length_encode should take a list and produce a run length encoded version
of that list. run_length_decode should then take a run length encoded list and
return the original list that would have produced it.

"""


def run_length_encode(ls):
    result = []
    current = [0, 0]
    for value in ls:
        if value == current[0]:
            current[1] += 1
        else:
            current = [value, 1]
            result.append(current)
    return result


def run_length_decode(ls):
    result = []
    for value, n in ls:
        for _ in range(n):
            result.append(value)
    return result
