class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        """ First idea:
        """
        pter1, pter2, pter3 = m, n, m + n
        while pter1 >= 1 and pter2 >= 1:
            if nums1[pter1 - 1] >= nums2[pter2 - 1]:
                nums1[pter3 - 1] = nums1[pter1 - 1]
                pter1 -= 1
            else:
                nums1[pter3 - 1] = nums2[pter2 - 1]
                pter2 -= 1
            pter3 -= 1
        if pter1 == 0:
            nums1[:pter2] = nums2[:pter2]

        """ More concise:
        """
        while m >= 1 and n >= 1:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if m == 0:
            nums1[:n] = nums2[:n]

        """ More concise:
        """
        while n > 0:
            if m <= 0 or nums1[m-1] <= nums2[n-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1

