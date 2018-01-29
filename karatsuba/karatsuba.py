import random
random.seed()

# Pi
A = 3141592653589793238462643383279502884197169399375105820974944592

# Euler's number
B = 2718281828459045235360287471352662497757247093699959574966967627


def karatsuba(A, B):
    if len(str(A)) < 2 or len(str(B)) < 2:
        return A * B
    else:
        n = max(len(str(A)), len(str(B)))
        m = n / 2
        magicNum = 10 ** m
        a = A / magicNum
        b = A % magicNum
        c = B / magicNum
        d = B % magicNum
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        quadLess = karatsuba(a+b, c+d) - ac - bd

    return 10**(2*m)  * ac +  10**m * quadLess + bd


product = karatsuba(A, B)
test = (product == A * B)
print product, test