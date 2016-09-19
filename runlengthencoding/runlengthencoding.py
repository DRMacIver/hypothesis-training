"""This module provides a pair of functions for converting lists to and from a
"run length encoding" format, where successive runs of the same value are
represented by that value followed by a count of how many times in a row it
should appear.

For example, the list [1, 1, 3, 1] in run-length encoded form is
[[1, 2], [3, 1], [1, 1]].

run_length_encode should take a list and produce a run length encoded version
of that list. run_length_decode should then take a run length encoded list and
return the original list that would have produced it.

"""


def run_length_encode(ls):
    """Return a run length encoded version of ls, as a list of pairs where the
    second element is the length of a run.. e.g. [a, a, b, c, c, c] =>
    [[a, 2], [b, 1], [c, 3]]"""
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
    """Decode a previously run length encoded list, giving the original list
    back. e.g. [a, a, b, c, c, c] => [a, a, b, c, c, c]"""
    result = []
    for value, n in ls:
        for _ in range(n):
            result.append(value)
    return result
