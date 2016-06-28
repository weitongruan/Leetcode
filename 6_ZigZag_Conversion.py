class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        """ Need to understand zigzag pattern. runtime: 116ms
        """
        if len(s) <= numRows or numRows == 1:
            return s
        else:
            rets = [''] * numRows

            index, step = 0, 1
            for element in s:
                rets[index] += element
                if index == 0:
                    step = 1
                elif index == numRows - 1:
                    step = -1
                index += step

            return ''.join(rets)


