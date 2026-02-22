class Solution:
    def binaryGap(self, n: int) -> int:
        prev = -1
        result = 0
        for curr in range(32):
            if ((n >> curr) & 1) > 0:
                if prev != -1:
                    result = max(result, curr - prev)
                prev = curr
                
        return result   