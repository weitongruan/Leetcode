def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """

    """ My solution:
    """
    return list(set(nums1).intersection(set(nums2)))

    """ Another solution online:
    """
    return list(set(nums1) & set(nums2))

def main():
    print intersection([1,2,3], [2,5,6])

main()
