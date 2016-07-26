def binaryAddition(digit1, digit2):
    return (digit1+digit2)/2, (digit1+digit2)%2
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        """ First idea: iterative algorithm: runtime: 96ms
        """
        idx = -1
        marker = 0
        stack = []
        ret = ""
        if len(a) < len(b):
            a, b = b, a
        while idx >= -len(a):
            if idx >= -len(b):
                if marker:
                    marker = binaryAddition(int(a[idx]), int(b[idx]) + 1)[0]
                    stack.append(binaryAddition(int(a[idx]), int(b[idx]) + 1)[1])
                else:
                    marker = binaryAddition(int(a[idx]), int(b[idx]))[0]
                    stack.append(binaryAddition(int(a[idx]), int(b[idx]))[1])
            else:
                if marker:
                    marker = binaryAddition(int(a[idx]), 1)[0]
                    stack.append(binaryAddition(int(a[idx]), 1)[1])
                else:
                    marker = 0
                    stack.append(int(a[idx]))
            idx -= 1
        if marker:
            stack.append(1)

        while stack:
            ret += str(stack.pop())

        return str(ret)

        """ A revised version: runtime: 80ms
        """
        idx = -1
        marker = 0
        stack = []
        ret = ""
        if len(a) < len(b):
            a, b = b, a
        while idx >= -len(a):
            if idx >= -len(b):
                stack.append(binaryAddition(int(a[idx]), int(b[idx]) + marker)[1])
                marker = binaryAddition(int(a[idx]), int(b[idx]) + marker)[0]
            else:
                if marker:
                    marker = binaryAddition(int(a[idx]), 1)[0]
                    stack.append(binaryAddition(int(a[idx]), 1)[1])
                else:
                    break
            idx -= 1
        if marker:
            stack.append(1)

        while stack:
            ret += str(stack.pop())

        return a[:idx + 1] + ret

