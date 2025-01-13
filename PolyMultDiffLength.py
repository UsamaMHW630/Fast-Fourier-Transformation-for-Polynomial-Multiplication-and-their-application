def PolyMultDiffLength(A,B):
    m = len(A)
    n = len(B)
    C = [0] * (m+n-1)
    for i in range(m):
        for j in range(n):
            C[i+j] += A[i]*B[j]

    #Remove the zeros at the end
    while len(C) > 1 and C[-1] == 0:
        C.pop(-1)

    return C
