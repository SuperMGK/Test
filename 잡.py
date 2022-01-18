import numpy as np

sample_road1 = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]

def solution(n, road, k):
    answer = 1
    max_cost = k
    matrix = np.full((n, n), 2222)
    for lists in road:
        node_1 = lists[0]
        node_2 = lists[1]
        distance = lists[2]
        matrix[(node_1 - 1, node_2 - 1)] = distance
        matrix[(node_2 - 1, node_1 - 1)] = distance

    my_index = 0

    for a in matrix:
        a[:my_index] = 2222
        my_index += 1

    starts = []
    su = []

    index = -1

    for b in matrix[0]:
        index += 1
        if b <= max_cost:
            su.append([index, b])
            starts.append(index)
            answer += 1

    while starts:
        for a in starts:
            for b in su:
                index_2 = -1
                if b[0] == a:
                    for c in matrix[a]:
                        index_2 += 1
                        if c + b[1] <= max_cost:
                            su.append([index_2, c + b[1]])
                            starts.append(index_2)
                            answer += 1
            starts.remove(a)

    return answer

print(solution(5, sample_road1, 3))