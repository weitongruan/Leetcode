class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        """ my understanding, not suitable here
        """

        if len(nums1) and len(nums2):

            if len(nums1) >= len(nums2):
                long, short = nums1, nums2
            else:
                long, short = nums2, nums1

            res = []

            pter_l = pter_s = interval_end = 0
            while pter_l < len(long):
                while pter_s < len(short) and long[pter_l] != short[pter_s]:
                    pter_s += 1
                if pter_s < len(short) and long[pter_l] == short[pter_s]:
                    while pter_s + interval_end < len(short) and pter_l + interval_end < len(long) \
                            and long[pter_l + interval_end] == short[pter_s + interval_end]:
                        interval_end += 1
                    res.append(short[pter_s:pter_s + interval_end])
                    pter_l = pter_l + interval_end - 1
                pter_s = interval_end = 0
                pter_l += 1
            return res
        else:
            return None

        """ Correct answer, using hashmap
        """
        dic = {}
        for n in nums1:
            dic[n] = dic.get(n, 0) + 1

        ret = []
        for n in nums2:
            if dic.get(n, 0):
                ret.append(n)
                dic[n] -= 1
        return ret

