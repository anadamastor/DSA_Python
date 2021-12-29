# Rotat a matrix by 90 degres
import numpy as np

matr = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def rotate_matrix_in(matr):
    print("In place approach: \n", np.matrix(matr))
    n = len(matr) 
    for i in range(n): # i are rows
        for j in range(i):
            matr[i][j], matr[j][i] = matr[j][i], matr[i][j]
    print(np.matrix(matr))

# rotate_matrix_in(matr)




def rotate_matrix(matr):
    print("Using a second matrix: \n", np.matrix(matr))
    new_arr = [[0,0,0],[0,0,0],[0,0,0]]
    n = len(matr)
    for i in range(n): # i are rows
        for j in range(n): 
            new_arr[i][j] = matr[j][j]
    print("New array: \n", np.matrix(new_arr))


if __name__ == "__main__":
    rotate_matrix(matr) 