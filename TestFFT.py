import unittest
import random
from PolyMultSameLength import PolyMultSameLength
from MultFFT import PolyMultFFT

class TestPolynomialMultiplication(unittest.TestCase):
    def test_random_polynomials(self):
        """
        Test polynomial multiplication multiple times for random polynomials
        of lengths that are powers of 2.
        """
        for _ in range(10):  # Run the entire test 10 times
            for n in [2, 4, 8, 16]:  # Polynomial lengths: powers of 2
                A = [random.randint(-10, 10) for _ in range(n)]
                B = [random.randint(-10, 10) for _ in range(n)]
                
                with self.subTest(length=n, A=A, B=B):
                    # Compute results using both methods
                    naive_result = PolyMultSameLength(A, B)
                    fft_result = PolyMultFFT(A, B)

                    # Assert that both results are the same
                    self.assertTrue(
                        all(abs(x - y) < 1e-6 for x, y in zip(naive_result, fft_result)),
                        f"Mismatch for A={A}, B={B}, Naive={naive_result}, FFT={fft_result}"
                    )

if __name__ == "__main__":
    unittest.main()
