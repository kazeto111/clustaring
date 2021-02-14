import numpy as np
import copy

input_data = []
while True:
    val = list(map(float, input().split()))
    if val:
        input_data.append(val)
    else:
        break

input_data = np.array(input_data)
ipsiron = float(input())
minPts = int(input())
data_size = len(input_data)
print("入力終わり", data_size)

distance_matrix = np.zeros((data_size, data_size), dtype=float)
for i in range(data_size):
    for j in range(i-1):
        distance_matrix[i][j] = np.sqrt(((input_data[i] - input_data[j])**2).sum())

already_searched = set([]) #探査済みの点の集合
clustaring_result = np.full(data_size, -1, dtype=int)
clustar_number = 0
for i in range(data_size):
    if i not in already_searched:
        if np.count_nonzero((distance_matrix[i] > 0) & (distance_matrix[i] < ipsiron)) < minPts:
            already_searched.add(i)
        else:
            a = np.where((distance_matrix[i] > 0) & (distance_matrix[i] < ipsiron))[0]
            #print(type(a))
            NeighborPts = set(a.tolist())
            while True:
                if NeighborPts <= already_searched:
                    break
                else:
                    c = copy.copy(NeighborPts)
                    for j in c:
                        if j not in already_searched:
                            already_searched.add(j)
                            if np.count_nonzero((distance_matrix[j] > 0) & (distance_matrix[j] < ipsiron)) >= minPts:
                                b = set((np.where((distance_matrix[j] > 0) & (distance_matrix[j] < ipsiron))[0]))
                                for k in b:
                                    NeighborPts.add(k)

                            clustaring_result[j] = clustar_number
            clustar_number += 1

print(clustaring_result.tolist())





