def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    """ My solution:
    """
    newlist = set()
    for num in nums:
        if num not in newlist:
            newlist.add(num)
        else:
            newlist.remove(num)
    return list(newlist)

    """ Use bitwise XOR:
    """
    rets = [0, 0]
    xor = reduce(lambda x, y: x ^ y, nums)
    setbit = 1
    while xor & setbit == 0:
        setbit = setbit << 1
    for num in nums:
        if num & setbit == 0:
            rets[0] ^= num
        else:
            rets[1] ^= num
    return rets

def main():
    print singleNumber([2, 1, 2, 3, 4, 1])

main()