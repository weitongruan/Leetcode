def plus(digit):
    return (digit + 1)/10, (digit + 1)%10
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        """ First idea: a recursive algorithm:
        """



        """ Second idea: an iterative algorithm: runtime 56ms
        """
        ret = []
        stack = []
        idx = -1
        marker = 1
        while idx >= -len(digits):
            if ((digits[idx]) + 1) / 10 == 1 and marker:
                stack.append(0)
                marker = 1
            elif marker:
                stack.append(digits[idx] + 1)
                marker = 0
            elif not marker:
                stack.append(digits[idx])
            idx -= 1
        if marker:
            stack.append(1)

        while stack:
            ret.append(stack.pop())
        return ret

        """ Third idea: a trick - careful, might result in an overflow, runtime: 52ms
        """
        num = 1
        for idx in xrange(len(digits)):
            num += digits[idx] * pow(10, len(digits) - idx - 1)
        return [int(digit) for digit in str(num)]






