class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D": 500, "M": 1000}

        result = dict[s[-1]]
        i = len(s) - 2
        while i >= 0:
            if dict[s[i]]  >= dict[s[i+1]]:
                result += dict[s[i]]
            else:
                result -= dict[s[i]]

            i -= 1

        return result


s = Solution()
print s.romanToInt("MCMXCIV")