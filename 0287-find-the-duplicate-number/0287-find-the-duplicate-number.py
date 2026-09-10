class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=set()
        for i in nums:
            if i in m:
                return i
            m.add(i)
                