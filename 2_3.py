import numpy as np
import random
import time

#中心は原点, 半径は1
def k_means_hypersphere(data_size, d_size, k):
  input_data = np.zeros((data_size, d_size), dtype=float)
  for i in range(data_size):
      a =  np.random.normal(loc=0, scale=1, size=d_size)
      input_data[i] = (a / ((a**2).sum())**(1/2)) * ((np.random.rand()) ** (1/d_size))

  #print(input_data)

  central_list = np.zeros((k, d_size), dtype=float)
  central_index_list = np.full(k,-1, dtype=int) #初期中心として同じ点を選んでしまわないように既に選んだ点のインデックスを記録
  for i in range(k):
      while True:
          a = random.randint(0, data_size-1)
          if not a in central_index_list:
              break

      for j in range(d_size):
          central_list[i][j] = input_data[a][j]

      central_index_list[i] = a

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


  loop_count = 0
  while True:
      loop_count += 1
      clustaring_result = np.copy(clustaring(central_list))  #0から始まるクラスタ番号を格納
      new_central_list = np.copy(re_central_calc(clustaring_result))
      if np.allclose(central_list, new_central_list):
          #print("b")
          break
      else:
          central_list = np.copy(new_central_list)
          #print(clustaring_result, "\n")
          #print(central_list, "\n")

  MSE = 0
  for i in range(k):
      b = np.zeros((np.count_nonzero(clustaring_result == i), d_size), dtype=float)
      flag = 0
      for j in range(data_size):
          if clustaring_result[j] == i:
              b[flag] = np.copy(input_data[j])
              flag += 1

      MSE += ((b-b.mean())**2).sum()

  MSE = MSE/k




  print(clustaring_result)
  return loop_count, MSE

data_size_list = [1000, 10000, 20000]
d_size_list = [2, 10, 100]
k_list = [10, 100, 1000]
for i in data_size_list:
    for j in d_size_list:
        for l in k_list:
            print(i, j, l)
            start = time.time()
            loop_count, MSE = k_means_hypersphere(i,j,l)
            end = time.time()
            print("実行時間", end-start)
            print("ループ回数", loop_count)
            print("誤差二乗平均", MSE, "\n")