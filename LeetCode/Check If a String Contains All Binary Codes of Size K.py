class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        required_count = 2 ** k

        seen_codes = set()

        for i in range(len(s) - k + 1):
            substring = s[i : i + k]
            seen_codes.add(substring)
            
            if len(seen_codes) == required_count:
                return True

        return len(seen_codes) == required_count

# For one line code we can simplify the return statement as follows:
#         return len({s[i:i+k] for i in range(len(s) - k + 1)}) == 2**k   