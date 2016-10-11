class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.sum = []
        p = q = 0
        for i in nums:
            p = i
            q = p + q
            self.sum.append(q)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i:
            return self.sum[j] - self.sum[i - 1]
        else:
            return self.sum[j]



            # Your NumArray object will be instantiated and called as such:
            # numArray = NumArray(nums)
            # numArray.sumRange(0, 1)
            # numArray.sumRange(1, 2)