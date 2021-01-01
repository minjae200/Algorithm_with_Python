def rotate_a_matrix_by_180_degree(a):
    n = len(a)
    m = len(a[0])

    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[n-i-1][n-j-1] = a[i][j]
    return result