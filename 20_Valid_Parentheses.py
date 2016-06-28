class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """ First Idea: runtime: 44ms
        """
        list = []
        left = set(["(", "{", "["])
        right = set([")", "}", "]"])
        pair = [("(", ")"), ("[", "]"), ("{", "}")]
        for parenthesis in s:
            if parenthesis in left:
                list.append(parenthesis)
            else:
                if len(list) == 0 or (list.pop(), parenthesis) not in pair:
                    return False

        return True if not len(list) else False

        """ It's better to use a dictionary: runtime: 44ms
        """
        stack = []
        dic = {")": "(", "]": "[", "}": "{"}
        for parenthesis in s:
            if parenthesis in dic.values():
                stack.append(parenthesis)
            elif not stack or dic[parenthesis] != stack.pop():
                return False

        return not stack
