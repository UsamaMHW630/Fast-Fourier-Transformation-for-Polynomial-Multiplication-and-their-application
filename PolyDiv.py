from MultFFT import PolyMultFFT
import math 

def polynomial_reversal(g):

    # Reverse the coefficients of a polynomial.

    n = len(g) - 1  # Degree of polynomial
    revG = [0] * (n + 1)  # Initialize reversed array
    for i in range(n + 1):
        revG[n - i] = g[i]  # Reverse coefficients
    return revG


def polynomial_division(f, revG):
    
    # Perform polynomial division using FFT and iterative updates.
    
    L = len(f) - len(revG) + 1  # Degree difference + 1
    G1 = [revG[i] if i < len(revG) else 0 for i in range(len(revG))]  # Subtract constant
    G1[0] -= 1  # G1 = revG - 1
    H = [[]] * (2*L + 1)  # Initialize H array
    H[2] = [1] + [-x for x in G1]  # H[2] = 1 - G1
    R1 = G1[:]  # Initialize R1
    k = 2

    while k <= L:
        k *= 2
        # Update R1 using FFT-based polynomial multiplication
        R1 = PolyMultFFT(R1, R1)
        # Update H[k]
        Hk_half = H[math.floor(k / 2)]  # Use integer division
        H[k] = [Hk_half[i] + PolyMultFFT(Hk_half, R1)[i] for i in range(len(Hk_half))]

    return H[k]
