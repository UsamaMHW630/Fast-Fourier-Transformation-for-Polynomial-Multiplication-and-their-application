# Polynomial Multiplication Algorithms

This repository contains implementations of various algorithms for polynomial multiplication and division, including:
- **Naive Multiplication**
- **Karatsuba Algorithm**
- **Fast Fourier Transform (FFT)**

These algorithms are analyzed and compared based on their theoretical and practical performance, as part of a thesis on efficient polynomial operations.

---

## Repository Structure

```plaintext
├── src/
│   ├── FFTandIFFT.py           # Implements FFT and IFFT
│   ├── Graph.py                # Plots runtime comparisons of the algorithms
│   ├── KaratsubaPoly.py        # Implements Karatsuba algorithm
│   ├── MultFFT.py              # Uses FFT for polynomial multiplication
│   ├── NormGraph.py            # Generates normalized performance plots
│   ├── PolyDiv.py              # Implements polynomial division
│   ├── PolyMultDiffLength.py   # Multiplies polynomials of different lengths
│   ├── PolyMultSameLength.py   # Multiplies polynomials of the same length
│
├── tests/
│   ├── Test_Karatsuba.py       # Unit tests for Karatsuba algorithm
│   ├── TestFFT.py              # Unit tests for FFT-based multiplication
│
├── README.md                   # This file
