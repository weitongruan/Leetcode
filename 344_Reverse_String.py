def reverseString(s):
    """
    :type s: str
    :rtype: str
    """

    """ My solution:
    """
    # print s
    newlist = list(s)
    # print newlist
    newlist.reverse()
    # print newlist

    return ''.join(newlist)

    """ one line solution: Extended slice
    """
    print s[::-1]

def main():
    print reverseString('hello')

main()
