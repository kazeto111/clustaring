import numpy as np
import random
#入力
input_data = []
while True:
    val = list(map(float, input().split()))
    if val:
        input_data.append(val)
    else:
        break

input_data = np.array(input_data, dtype=float)
#print(input_data)
data_size = len(input_data)
d_size = len(input_data[0])
k = int(input())

central_list = np.zeros((k, d_size), dtype=float)
for i in range(k):
    for j in range(d_size):
        central_list[i][j] = input_data[random.randint(0, data_size-1)][j]

#クラスタリングと代表点再計算

#central_listの点を中心とたクラスタリング結果をclustaring_resultに書き込む関数clustaringの定義
#メモリ消費を抑えるためclustaringで使う行列をglobalで定義
distance_matrix = np.zeros((k, data_size), dtype=float)
#distance_matrixはi番目のデータのj番目の代表点からの距離がそれぞれ格納された行列

def clustaring(central_list):
    for i in range(k):
        distance_matrix[i] = ((input_data - central_list[i])**2).sum(axis=1)
    a = np.argmin(distance_matrix, axis=0)
    return a

#新しい重点を計算する関数
def re_central_calc(clustaring_result):
    a = np.zeros((k, d_size), dtype=float)
    for i in range(k):
        b = np.zeros((np.count_nonzero(clustaring_result==i), d_size), dtype=float)
        flag = 0
        for j in range(data_size):
            if clustaring_result[j] == i:
                b[flag] = np.copy(input_data[j])
                flag += 1
        a[i] = b.mean(axis=0)

    del b
    return a








clustaring_result = np.zeros(data_size, dtype=int) #0から始まるクラスタ番号を格納
while True:
    clustaring_result = np.copy(clustaring(central_list))
    new_central_list = np.copy(re_central_calc(clustaring_result))
    if np.allclose(central_list, new_central_list):
        #print("b")
        break
    else:
        central_list = np.copy(new_central_list)
        #print(clustaring_result, "\n")
        #print(central_list, "\n")


print(clustaring_result)
