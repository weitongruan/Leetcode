def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    """ My solution: This definitely requires extra memory
    """
    pot_set = set()
    for integer in nums:
        if integer not in pot_set:
            pot_set.add(integer)
        else:
            pot_set.remove(integer)
    return pot_set.pop()

    """ in place implementation: use bitwise XOR
    """
    return reduce(lambda x, y: x ^ y, nums)
