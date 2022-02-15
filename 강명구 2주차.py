import numpy as np

sample_road1 = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
sample_road2 = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]

def solution(n, road, k):
    max_cost = k # 최대 이동 거리
    matrix = np.full((n, n), 2222) # 마을과 마을 사이의 거리를 나타내는
    for lists in road:
        node_1 = lists[0]
        node_2 = lists[1]
        distance = lists[2] # ? 에서 ? 까지 거리는 ?
        if matrix[(node_1 - 1, node_2 - 1)] != 2222:
            matrix[(node_1 - 1, node_2 - 1)] = min([matrix[(node_1 - 1, node_2 - 1)], distance])
        else:
            matrix[(node_1 - 1, node_2 - 1)] = distance

        if matrix[(node_2 - 1, node_1 - 1)] != 2222:
            matrix[(node_2 - 1, node_1 - 1)] = min([matrix[(node_2 - 1, node_1 - 1)], distance])
        else:
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
            su.append((0, index, b))
            starts.append(index)


    while starts:
        for a in starts:
            for b in su:
                index_2 = -1
                if b[1] == a:
                    for c in matrix[a]:
                        index_2 += 1
                        if c + b[2] <= max_cost:
                            su.append((b[1], index_2, c + b[2]))
                            starts.append(index_2)
            starts.remove(a)



    answer = []
    for v in su:
        answer.append(v[1])

    answer = set(answer)
    return 1 + len(answer)

print(solution(5, sample_road1, 3))
print(solution(6, sample_road2, 4))