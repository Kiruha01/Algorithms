ORDER = ['a', 'b']


def step(digits, permutation):
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
    return counts

    # new_permutation = [0,0,0]
    # for i in permutation:
#
# with open('input.txt') as filein:
#     N, M, K = map(int, filein.readline().split())
#     for i in range(M):
