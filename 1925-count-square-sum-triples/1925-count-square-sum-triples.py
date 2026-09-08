class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        for i in range(1,n+1):
            for j in range(1,n+1):
                k=int((i*i+j*j)**0.5)
                if k<=n and k*k==i*i+j*j:
                    count+=1
        return count