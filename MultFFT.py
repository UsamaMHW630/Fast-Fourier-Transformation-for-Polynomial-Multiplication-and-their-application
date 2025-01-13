import cmath

from PolyMultSameLength import PolyMultSameLength
from FFTandIFFT import FFT
from FFTandIFFT import IFFT
from FFTandIFFT import normalized_real_IFFT

def next_power_of_two(x):
    return 1 << (x - 1).bit_length()

def PolyMultFFT(A, B):
    m = len(A) + len(B) - 1
    fft_size = next_power_of_two(m)

    A_padded = A + [0] * (fft_size - len(A))
    B_padded = B + [0] * (fft_size - len(B))

    FFT_A = FFT(A_padded)
    FFT_B = FFT(B_padded)
    FFT_C = [FFT_A[i] * FFT_B[i] for i in range(fft_size)]
    result = normalized_real_IFFT(FFT_C)

    return result[:m]  # Trim to correct length
