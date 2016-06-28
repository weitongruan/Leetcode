class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        """ First idea: runtime: 76ms
        """
        if len(strs) == 0:
            return ""
        else:
            minlength = min([len(str) for str in strs])

            index = 0
            while index < minlength:
                if len(set([str[index] for str in strs])) == 1:
                    index += 1
                else:
                    return strs[0][:index]
            return strs[0][:index]

        """ An idea online, use zip: runtime: 56ms
        """
        if len(strs) == 0:
            return ""
        else:
            ret = ""
            for element in zip(*strs):
                if len(set(element)) == 1:
                    ret += set(element).pop()
                else:
                    return ret

            return ret


