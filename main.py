ORDER = ['a', 'b']


def step(digits, perm):
    counts = dict(zip(ORDER, [0]*len(ORDER)))
    for d in digits:
        counts[d] += 1

    temp = 0
    prev = 0
    for d in ORDER:
        position = temp + prev
        temp = counts[d]
        prev = position
        counts[d] = position

    new_permutation = [0] * len(perm)
    for idx in perm:
        digit = digits[idx]
        new_permutation[counts[digit]] = idx
        counts[digit] += 1

    return new_permutation


def main():
    with open('input.txt', 'r') as filein:
        # N - число строк, M - длина строк, K - число фаз итераций
        N, M, K = map(int, filein.readline().split())
        lines = []
        for i in range(M):
            line = filein.readline().rstrip('\n')
            lines.insert(0, line)

    permutation = [i for i in range(N)]

    for i, line in zip(range(K), lines):
        permutation = step(line, permutation)

    with open('output.txt', 'w') as fileout:
        for i, _ in enumerate(permutation):
            permutation[i] = str(permutation[i] + 1)
        fileout.write(' '.join(permutation))


if __name__ == '__main__':
    main()