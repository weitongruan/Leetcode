def transform(strings):
    ret = ""
    slow = fast = 0
    while fast < len(strings):
        if strings[fast] == strings[slow]:
            fast += 1
        else:
            ret += str(fast - slow)+strings[slow]
            slow = fast
    if fast - slow:
        ret += str(fast - slow)+strings[slow]
    return ret

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        """ First idea: recursive call a function transform(): runtime: 72ms
        """
        if n == 1:
            return "1"
        else:
            return transform(self.countAndSay(n-1))

