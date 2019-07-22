class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {")": "(", "]": "[", "}":"{"}
        stack = []
        for c in s:
            if dict.has_key(c):
                if len(stack) > 0:
                    if stack.pop() != dict[c]:
                        return False
                    else:
                        pass
                else:
                    return False
            else:
                stack.append(c)

        if 0 == len(stack):
            return True
        else:
            return False

str = "()[]{}"
# str = "([)]"
s = Solution()
print s.isValid(str)