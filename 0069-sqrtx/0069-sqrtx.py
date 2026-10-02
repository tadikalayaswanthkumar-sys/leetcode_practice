class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        result = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if mid * mid > x:
                # The square of mid is too large, search the lower half
                right = mid - 1
            elif mid * mid < x:
                # The square of mid is smaller, it's a candidate for the rounded-down root
                # Search the upper half to see if there's a closer match
                left = mid + 1
                result = mid
            else:
                # Exact match found
                return mid
                
        return result