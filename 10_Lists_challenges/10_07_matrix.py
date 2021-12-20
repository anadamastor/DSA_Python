# Rotat a matrix by 90 degres

matr = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def rotate_matrix(matr):
    print(matr)
    for i in range(0,len(matr)):
        # rotation for corners
        for j in range(i):
            #rotation  for centers
            matr[i][j], matr[i][-1] = matr[i][-1], matr[i][0]
            matr[i][1], matr[j][1] = matr[j][1], matr[i][1]
    print(matr)

rotate_matrix(matr)
