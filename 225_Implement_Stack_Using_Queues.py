class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        for i in xrange(len(self.stack) - 1):
            self.stack.append(self.stack[0])
            self.stack.pop(0)

    def pop(self):
        """
        :rtype: nothing
        """
        self.stack.pop(0)

    def top(self):
        """
        :rtype: int
        """
        return self.stack[0]

    def empty(self):
        """
        :rtype: bool
        """
        return self.stack == []
