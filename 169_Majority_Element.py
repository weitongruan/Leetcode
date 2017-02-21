class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """ First idea: runtime: 208ms
        """
        return heapq.nlargest(1, Counter(nums), key=lambda x: Counter(nums)[x])[0]

        """ Second idea: rumtime: 84ms
        """
        return Counter(nums).most_common(1)[0][0]
        """ A short one online:
        """
        return sorted(num)[len(num) / 2]

        """ Bit Manipulation
        """

        def majorityElement(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """

            bits = [0] * 32
            for num in nums:
                for i in xrange(32):
                    bits[i] += (num >> i) & 1

            result = 0
            for j, val in enumerate(bits):
                if val > len(nums) / 2:
                    if j == 31:
                        result = -((1 << 31) - result)
                    else:
                        result |= 1 << j

            return result