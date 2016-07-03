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
