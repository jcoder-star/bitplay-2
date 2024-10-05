def reverse_bits(n):
    result = 0
    bit_length = n.bit_length()  # Get the number of bits required to represent n
    
    for i in range(bit_length):
        # Get the i-th bit from the right and shift it to the left position in the result
        result <<= 1  # Shift result left to make room for the next bit
        result |= (n & 1)  # Add the rightmost bit of n to result
        n >>= 1  # Shift n right to process the next bit

    return result

# Example usage
number = 18  # Binary: 10010
reversed_number = reverse_bits(number)

print(f"The original number: {number} (binary: {bin(number)})")
print(f"The reversed bits number: {reversed_number} (binary: {bin(reversed_number)})")

