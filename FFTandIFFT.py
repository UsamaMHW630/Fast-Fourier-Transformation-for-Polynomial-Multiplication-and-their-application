import cmath

def FFT(P, decimals=4):
    n = len(P)
    if n == 1:
        return P
    # Use omega for FFT
    omega_n = cmath.exp((2j * cmath.pi) / n)
    omega = 1

    Aeven = P[::2]
    Aodd = P[1::2]
    
    Yeven = FFT(Aeven, decimals)
    Yodd = FFT(Aodd, decimals)

    y = [0] * n

    for i in range(n // 2):
        y[i] = Yeven[i] + omega * Yodd[i]
        y[i + n // 2] = Yeven[i] - omega * Yodd[i]
        omega *= omega_n  # Update omega to omega^(i+1)

    # Format the result to specified decimal places
    return [complex(round(value.real, decimals), round(value.imag, decimals)) for value in y]

def IFFT(P):
    n = len(P)
    if n == 1:
        return P
    # Use omega^(-1) for IFFT
    omega_n = cmath.exp((-2j * cmath.pi) / n)
    omega = 1

    Aeven = P[::2]
    Aodd = P[1::2]
    
    Yeven = IFFT(Aeven)
    Yodd = IFFT(Aodd)

    y = [0] * n

    for i in range(n // 2):
        y[i] = Yeven[i] + omega * Yodd[i]
        y[i + n // 2] = Yeven[i] - omega * Yodd[i]
        omega *= omega_n  # Update omega to omega^(i+1)

    return y

def normalized_real_IFFT(P, decimals=4, threshold=1e-6):
    """
    Perform IFFT, normalize, and round results. 
    Use a threshold to handle small numerical artifacts.
    """
    n = len(P)
    raw_output = IFFT(P)
    
    # Normalize and handle numerical artifacts
    result = []
    for value in raw_output:
        normalized_value = value.real / n
        # Clamp small values to zero
        if abs(normalized_value) < threshold:
            normalized_value = 0
        # Round to the nearest integer
        result.append(round(normalized_value))
    return result
