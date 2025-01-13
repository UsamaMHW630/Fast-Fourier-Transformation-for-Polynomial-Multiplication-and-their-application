import unittest
import random

# Import your functions here (assuming they're in the same directory)
from KaratsubaPoly import karatsuba_poly
from PolyMultSameLength import PolyMultSameLength
from PolyMultDiffLength import PolyMultDiffLength

def randomArray(length):
    return [random.randint(-10,10) for _ in range(length)]

class TestPolynomialMultiplication(unittest.TestCase):
    
    def test_karatsuba_sameL_vs_naive(self):
        # Generate random polynomials
        for _ in range(10):  # Run the test 10 times with random inputs
            A = randomArray(4)
            B = randomArray(4)
            
            # Get the results of both algorithms
            karatsuba_result = karatsuba_poly(A, B)
            naive_result = PolyMultSameLength(A, B)
            
            # Assert that the results are the same
            self.assertEqual(karatsuba_result, naive_result, f"Failed for A: {A}, B: {B}")
    
    def test_karatsuba_sameL_fixed(self):
        # Test with known polynomials
        A = [1, 2, 3, 4]
        B = [5, 6, 7, 8]
        
        expected_result = PolyMultSameLength(A, B)  # Using the direct method as a reference
        
        karatsuba_result = karatsuba_poly(A, B)
        self.assertEqual(karatsuba_result, expected_result, "Karatsuba same length result mismatch for fixed inputs.")

    def test_karatsuba_diffL_vs_naive(self):
        # Generate random polynomials
        for _ in range(10):  # Run the test 10 times with random inputs
            A = randomArray(3)
            B = randomArray(4)
            
            # Get the results of both algorithms
            karatsuba_result = karatsuba_poly(A, B)
            naive_result = PolyMultDiffLength(A, B)
            
            # Assert that the results are the same
            self.assertEqual(karatsuba_result, naive_result, f"Failed for A: {A}, B: {B}")
    
    def test_karatsuba_diffL_fixed(self):
        # Test with known polynomials
        A = [1, 2, 3]
        B = [4, 5, 6, 7]
        
        expected_result = PolyMultDiffLength(A, B)  # Using the direct method as a reference
        karatsuba_result = karatsuba_poly(A, B)
        self.assertEqual(karatsuba_result, expected_result, "Karatsuba different length result mismatch for fixed inputs.")


if __name__ == '__main__':
    unittest.main()