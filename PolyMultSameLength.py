def PolyMultSameLength(A,B):
    n = len(A)
    C = [0] * (2*n-1)
    for i in range(n):
        for j in range(n):
            C[i+j] += A[i]*B[j]

    #Remove the zeros at the end
    while len(C) > 1 and C[-1] == 0:
        C.pop(-1)

    return C

