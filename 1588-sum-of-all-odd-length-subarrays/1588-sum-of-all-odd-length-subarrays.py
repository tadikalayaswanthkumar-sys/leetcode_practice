class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        total = 0
        n = len(arr)

        for i in range(n):
            current_sum = 0

            for j in range(i, n):
                current_sum += arr[j]

                length =j  - i + 1

                if length % 2 == 1:
                    total += current_sum

        return total