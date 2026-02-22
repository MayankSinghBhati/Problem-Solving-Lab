class Solution:
    def isPalindrome(self, x: int) -> bool:
        xstr=str(x)
        if xstr == xstr[::-1]:
            return True
        else :
            return False