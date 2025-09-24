


def compareVersion(version1: str, version2: str) -> int:
    # Step 1: Split into parts
    v1 = version1.split('.')
    v2 = version2.split('.')

    # Step 2: Convert to integers (ignores leading zeros)
    v1 = [int(num) for num in v1]
    v2 = [int(num) for num in v2]

    # Step 3: Equalize lengths
    max_len = max(len(v1), len(v2))
    while len(v1) < max_len:
        v1.append(0)
    while len(v2) < max_len:
        v2.append(0)

    # Step 4: Compare element by element
    for i in range(max_len):
        if v1[i] < v2[i]:
            return -1
        elif v1[i] > v2[i]:
            return 1

    # Step 5: All equal
    return 0
