class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a=str(x)
        s=""
        for i in range(len(a)-1,-1,-1):
            s+=a[i]
        if s==a:
            return True
        else:
            return False
            
         