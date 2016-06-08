def canWinNim(n):
    """
    :type n: int
    :rtype: bool
    """

    """ My solution:
    """
    return False if n % 4 == 0 else True

    """ Other solution:
    """
    return bool(n % 4)
    """ or
    """
    return n % 4 != 0


def main():
    print canWinNim(15)

main()
