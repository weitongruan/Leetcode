class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        for _ in xrange(len(self.queue2)):
            self.queue1.append(self.queue2[-1])
            self.queue2.pop()

        self.queue1.append(x)

        for _ in xrange(len(self.queue1)):
            self.queue2.append(self.queue1[-1])
            self.queue1.pop()

    def pop(self):
        """
        :rtype: nothing
        """
        self.queue2.pop()

    def peek(self):
        """
        :rtype: int
        """
        return self.queue2[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return self.queue2 == []