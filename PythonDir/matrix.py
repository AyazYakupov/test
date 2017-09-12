
import numpy as np


n = int(input("Это матрица размером 2n-1 * 2n-1. Введите n: "))
side = 2*n-1
size = (2*n-1)*(2*n-1)
number = 1
matrix = np.eye(side)

print(matrix)
# for i in range(side):
#     for j in range(side):
#         matrix[i][j] = 0
#         print(matrix[i][j],end='')
#     print('\n')

# for i in range(side):


