'''Reverse bits of a given 32 bits unsigned integer.

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.'''

def reverse_bits(n: int):
        ans = 0
        for i in range(32):
            ans = (ans << 1) | (n & 1)
            n >>= 1
       
        return ans

#moving bit to bit

n = 00000010100101000001111010011100
print(reverse_bits(n))