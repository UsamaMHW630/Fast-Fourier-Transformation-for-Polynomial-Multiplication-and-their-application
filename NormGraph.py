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

# Measure runtime for each algorithm
power_range = (1, 10)  # Polynomial sizes: 2^1 to 2^13
sizes = powers_of_two(*power_range)  # Sizes as powers of 2

# Timing lists
times_naive = []
times_karatsuba = []
times_fft = []

# Measure times
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

# Calculate average naive time
average_naive_time = sum(times_naive) / len(times_naive)

# Normalize times by naive average
times_karatsuba_normalized = [t / average_naive_time for t in times_karatsuba]
times_fft_normalized = [t / average_naive_time for t in times_fft]

# Scale polynomial sizes to make naive average equal 1
scaled_sizes = [s / sizes[-1] for s in sizes]

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(scaled_sizes, times_karatsuba_normalized, label="Karatsuba (normalized)", marker="s")
plt.plot(scaled_sizes, times_fft_normalized, label="FFT (normalized)", marker="^")
plt.xlabel("Scaled Polynomial Size (Normalized)")
plt.ylabel("Time (Normalized to Naive Average)")
plt.title("Normalized Performance of Polynomial Multiplication Algorithms")
plt.legend()
plt.grid()
plt.show()
