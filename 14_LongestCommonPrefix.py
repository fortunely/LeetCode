class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common_prefix = []

        if len(strs) == 0:
            return ""
        else:
            for i in range(0, len(strs[0])):
                c = strs[0][i]

                # c_is_common_prefix = False
                for s in strs[1:]:
                    if i < len(s): # with the sub string s
                        if c == s[i]:
                            pass
                        else:
                            return "".join([substr for substr in common_prefix])
                    else: # overflow than any sub string s
                        return "".join([substr for substr in common_prefix])

                # all substrings own the character c
                common_prefix.append(c)

        return "".join([substr for substr in common_prefix])


strs = ["flower","flow","flight"]
# strs = ["dog","racecar","car"]
strs = ["aa", "a"]
s = Solution()
print s.longestCommonPrefix(strs)