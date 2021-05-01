def step(digits, permutation):
    counts = {}
    for d in digits:
        if d in counts:
            counts[d] += 1
        else:
            counts[d] = 1

    temp = 0
    prev = 0
    for d in counts.keys():
        position = temp + prev
        temp = counts[d]
        prev = position
        counts[d] = position

    new_permutation = [0,0,0]
    for i in permutation:


with open('input.txt') as filein:
    N, M, K = map(int, filein.readline().split())
    for i in range(M):
