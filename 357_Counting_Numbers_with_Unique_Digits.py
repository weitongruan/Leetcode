# import math
def countNumbersWithUniqueDigits(n):
    """
    :type n: int
    :rtype: int
    """
    """ My first solution (Recursion): Runtime 72ms
    """
    if n == 0:
        return 1
    elif n == 1:
        return 10
    elif n > 10:
        return countNumbersWithUniqueDigits(10)
    else:
        return countNumbersWithUniqueDigits(n - 1) + 9 * math.factorial(9) / math.factorial(10 - n)

    """ replace the factorial() with a loop: Still runtime 48ms
    """
    if n == 0:
        return 1
    elif n == 1:
        return 10
    elif n > 10:
        return countNumbersWithUniqueDigits(10)
    else:
        s = 1
        for idx in xrange(9, 10 - n, -1):
            s *= idx
        return countNumbersWithUniqueDigits(n - 1) + 9 * s

    """ Don't use recursion, use loop runtime: 68ms
    """
    if n == 0:
        return 1
    if n == 1:
        return 10
    if n > 10:
        return countNumbersWithUniqueDigits(10)
    else:
        out = 10
        for idx in xrange(2, n + 1):
            s = 1
            for jdx in xrange(9, 10 - idx, -1):
                s *= jdx
                print s
            out += 9 * s
        return out
    """ Only one loop sufices: rumtime: 64ms
    """
    if n == 0:
        return 1
    if n == 1:
        return 10
    if n > 10:
        return countNumbersWithUniqueDigits(10)
    else:
        out = 10
        temp = 9
        for idx in xrange(2, n + 1):
            temp *= (11 - idx)
            out += temp
        return out

def main():
    print countNumbersWithUniqueDigits(3)

main()