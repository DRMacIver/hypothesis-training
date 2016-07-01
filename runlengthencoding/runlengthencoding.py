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
