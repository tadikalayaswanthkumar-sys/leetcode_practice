class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        l = nums1 + nums2
        l.sort()

        if len(l) % 2 == 0:
            s = len(l) // 2
            return (l[s] + l[s - 1]) / 2
        else:
            s = len(l) // 2
            return l[s]