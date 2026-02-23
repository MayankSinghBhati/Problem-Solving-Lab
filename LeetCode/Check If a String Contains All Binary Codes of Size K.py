class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if k>1:
            for i in range(len(s)):
                if s[i] == s[i+1]:
                    return True
                else:
                    return False
        else:
            return True
