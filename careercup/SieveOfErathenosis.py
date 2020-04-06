"""

Find prime number upto N

Time Complexity ::: O(nlog(log n))

"""

class Sieve:
    def primes(self,N):
        resp = []
        primes = [True] * N

        for i in range(2,N):
            if primes[i]:
                j=i*i
                while j<N:
                    primes[j] = False
                    j += i
        for i in range(2,len(primes)):
            if primes[i]:
                resp.append(i)
        return resp


sol = Sieve()
print(sol.primes(100))