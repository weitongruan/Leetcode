class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not numbers:
            return None
        else:
            index1 = 0
            index2 = len(numbers) - 1
            while index1 < index2:
                if numbers[index1] + numbers[index2] == target:
                    return index1 + 1, index2 + 1
                elif numbers[index1] + numbers[index2] < target:
                    index1 += 1
                else:
                    index2 -= 1
