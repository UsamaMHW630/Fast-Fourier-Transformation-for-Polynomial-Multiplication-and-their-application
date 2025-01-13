def add_polynomials(A, B):
    # Make the lengths of both polynomials equal by appending 0s to the shorter one
    n = max(len(A), len(B))
    A += [0] * (n - len(A))
    B += [0] * (n - len(B))
    
    return [A[i] + B[i] for i in range(n)]

def subtract_polynomials(A, B):
    # Make the lengths of both polynomials equal by appending 0s to the shorter one
    n = max(len(A), len(B))
    A += [0] * (n - len(A))
    B += [0] * (n - len(B))
    
    return [A[i] - B[i] for i in range(n)]

def karatsuba_poly(A, B):
    n = max(len(A), len(B))
    
    
    # Base case when size is 1 (polynomials are just constants)
    if n == 1:
        return [A[0] * B[0]]
    
    # Make both A and B the same length by appending 0s to the shorter one
    A += [0] * (n - len(A))
    B += [0] * (n - len(B))
    
    # Split the polynomials into two halves
    m = n // 2
    A_low = A[:m]     # Lower half of A
    A_high = A[m:]    # Higher half of A
    B_low = B[:m]     # Lower half of B
    B_high = B[m:]    # Higher half of B
    
    # Recursively compute three products
    P1 = karatsuba_poly(A_low, B_low)  # A_low * B_low
    P2 = karatsuba_poly(A_high, B_high)  # A_high * B_high
    
    # Sum of the lower and higher parts
    A_sum = add_polynomials(A_low, A_high)
    B_sum = add_polynomials(B_low, B_high)
    
    P3 = karatsuba_poly(A_sum, B_sum)  # (A_low + A_high) * (B_low + B_high)
    
    # Combine the results: P3 - P1 - P2 goes in the middle
    middle_term = subtract_polynomials(subtract_polynomials(P3, P1), P2)
    
    # Final result array of size 2n - 1
    result = [0] * (2 * n - 1)
    
    # Add P1 (goes into the lower part)
    for i in range(len(P1)):
        result[i] += P1[i]
    
    # Add P2 (goes into the higher part)
    for i in range(len(P2)):
        result[i + 2 * m] += P2[i]
    
    # Add middle term (goes into the middle part)
    for i in range(len(middle_term)):
        result[i + m] += middle_term[i]
    
    #Remove the zeros at the end
    while len(result) > 1 and result[-1] == 0:
        result.pop(-1)

    return result
