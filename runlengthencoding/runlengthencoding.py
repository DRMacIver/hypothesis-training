"""
Tools for converting lists to and from a "run length encoding" format, where
successive runs of the same value are represented by:
    * that value
    * a count of how many times in a row it should appear.

For example, the list
    [1, 1, 3, 1]

in run-length encoded form is
    [[1, 2], [3, 1], [1, 1]]
"""


def run_length_encode(ls):
    """Convert list to run-length encoded representation"""
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
    """Decode run-length encoded list"""
    result = []
    for value, n in ls:
        for _ in range(n):
            result.append(value)
    return result
