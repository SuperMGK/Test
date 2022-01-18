import numpy as np

sample_map = np.array([[1, 0, 1, 1, 1, 0],
                       [1, 0, 1, 0, 1, 0],
                       [1, 1, 1, 0, 1, 0],
                       [0, 0, 1, 0, 1, 0],
                       [1, 1, 1, 0, 1, 1]])

def find_way(matrix):

    try:
        first_loc = (0, 0)
        direction = [np.array([1, 0]), np.array([0, 1]), np.array([-1, 0]), np.array([0, -1])]
        jina = []
        bungi = []

        while True:
            su = []


            for a in direction:
                b = tuple(np.array(first_loc) + a)
                if b[0] >= 0 and b[1] >= 0:
                    if b[0] != 0 or b[1] != 0:
                        if b[0] <= matrix.shape[0] - 1 and b[1] <= matrix.shape[1] - 1:
                            if b not in jina:
                                su.append(b)

            su2 = []

            for x in su:
                if matrix[x] == 1:
                    first_loc = x
                    su2.append(first_loc)

            if len(su2) >= 2:
                bungi = su2




            su3 = []

            for z in su2:
                distance = ((matrix.shape[0] - 1 - z[0]) ** 2 + (matrix.shape[1] - 1 - z[1]) ** 2) ** (1/2)
                su3.append(distance)

            if len(su3) == 0:
                bungi_loc = [item for item in bungi if item not in jina]
                first_loc = bungi_loc[0]
                jina.append(first_loc)
                continue

            tmp = min(su3)
            index = su3.index(tmp)
            first_loc = su2[index]

            jina.append(first_loc)

            if first_loc == (matrix.shape[0] - 1, matrix.shape[1] - 1):
                break

        result = jina

    except:
        result = -1

    return result



print(find_way(sample_map))