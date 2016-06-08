def addDigits(num):
    """
    :type num: int
    :rtype: int
    """

    """ My solution:
    """
    return 9 if (num % 9 == 0) & (num != 0) else num % 9

    """ Another good one:
    """
    return 0 if num == 0 else (num - 1) % 9 + 1


def main():
    print addDigits(9)

main()