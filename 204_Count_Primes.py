class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        """ First idea: Time limit exceeded
        """
        if n <= 2:
            return 0
        else:
            prime_set = set([2])
            for i in xrange(3, n):
                indicator = 0
                for j in prime_set:
                    if i % j == 0:
                        indicator = 1
                        break
                if not indicator:
                    prime_set.add(i)

            return len(prime_set)

        """ Second idea: time limit exceeded
        """
        if n <= 2:
            return 0
        else:
            prime_set = set([2])
            for i in xrange(3, n):
                indicator = 0
                for j in prime_set:
                    if j < (n) ** 0.5 + 1 and i % j == 0: # add one more condition
                        indicator = 1
                        break
                if not indicator:
                    prime_set.add(i)

            return len(prime_set)

        """ one algorithm online:
        """

        if n <= 2:
            return 0
        else:
            primes = n * [1]
            primes[0] = primes[1] = 0
            for i in xrange(2, int(n ** 0.5) + 1):
                if primes[i]:
                    primes[i * i:n:i] = [0] * len(primes[i * i:n:i])
            return sum(primes)
