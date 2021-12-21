# Rotat a matrix by 90 degres
import numpy as np

matr = [
    [0,2,3],
    [4,5,6],
    [7,8,9]
]

def diag_sum(arr):
    sum = 0
    for i in range(len(arr)):
        print(i)
        for j in range(len(arr)):
            if i == j:
                sum += arr[i][j]
    print(sum)

diag_sum(matr)