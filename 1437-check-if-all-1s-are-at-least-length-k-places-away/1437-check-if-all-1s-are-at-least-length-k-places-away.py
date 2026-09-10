class Solution(object):
    def kLengthApart(self, nums, k):
        prev = -1

        for i in range(len(nums)):
            if nums[i] == 1:

                if prev != -1 and i - prev <= k:
                    return False
                prev = i

        return True