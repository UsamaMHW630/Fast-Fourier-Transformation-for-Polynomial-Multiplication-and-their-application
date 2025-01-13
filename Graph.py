import matplotlib.pyplot as plt
import timeit
import random
import math
from PolyMultSameLength import PolyMultSameLength
from KaratsubaPoly import karatsuba_poly
from MultFFT import PolyMultFFT

# Generate random polynomials of size as powers of 2
def generate_random_poly(size):
    return [random.randint(-10, 10) for _ in range(size)]

# Get sizes that are powers of 2
def powers_of_two(start, end):
    return [2**i for i in range(start, end + 1)]

# Theoretical time complexities
def theoretical_naive(size):
    return size ** 2

def theoretical_karatsuba(size):
    return size ** math.log2(3)  # O(n^{log_2(3)})

def theoretical_fft(size):
    return size * math.log2(size)  # O(nlog_2(n))

# Measure runtime for each algorithm
power_range = (1, 13)  # Polynomial sizes: 2^1 to 2^13
sizes = powers_of_two(*power_range)  # Sizes as powers of 2
times_naive = []
times_karatsuba = []
times_fft = []

for size in sizes:
    poly1 = generate_random_poly(size)
    poly2 = generate_random_poly(size)

    # Naive Polynomial Multiplication
    t_naive = timeit.timeit(lambda: PolyMultSameLength(poly1, poly2), number=1)
    times_naive.append(t_naive)

    # Karatsuba Polynomial Multiplication
    t_karatsuba = timeit.timeit(lambda: karatsuba_poly(poly1, poly2), number=1)
    times_karatsuba.append(t_karatsuba)

    # FFT Polynomial Multiplication
    t_fft = timeit.timeit(lambda: PolyMultFFT(poly1, poly2), number=1)
    times_fft.append(t_fft)

# Practical time divided by theoretical time complexity
practical_theoretical_naive = [t / theoretical_naive(size) for t, size in zip(times_naive, sizes)]
practical_theoretical_karatsuba = [t / theoretical_karatsuba(size) for t, size in zip(times_karatsuba, sizes)]
practical_theoretical_fft = [t / theoretical_fft(size) for t, size in zip(times_fft, sizes)]


# Plot results
plt.figure(figsize=(10, 6))
plt.plot(sizes, practical_theoretical_naive, label="Naive", marker="o")
plt.plot(sizes, practical_theoretical_karatsuba, label="Karatsuba", marker="s")
plt.plot(sizes, practical_theoretical_fft, label="FFT", marker="^")
plt.xlabel("Polynomial Size (Power of 2)")
plt.ylabel("Practical/Theoretical Time Ratio")
plt.title("Comparison of Practical/Theoretical Time Ratios for Polynomial Multiplication")
plt.xticks(sizes, labels=[f"2^{int(i)}" for i in range(power_range[0], power_range[1] + 1)])
plt.legend()
plt.grid()
plt.show()
'''
print("practical_theoretical_naive", practical_theoretical_naive)
print("practical_theoretical_karatsuba", practical_theoretical_karatsuba)
print("practical_theoretical_fft", practical_theoretical_fft)
'''