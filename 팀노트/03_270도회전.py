def rotate_a_matrix_by_270_degree(a):
    n = len(a)
    m = len(a[0])

    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j-i-1][i] = a[i][j]
    return result