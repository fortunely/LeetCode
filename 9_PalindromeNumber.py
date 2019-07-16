class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_origin = x
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            reverse_num = 0
            while 0 != x:
                num = x % 10
                x = x / 10
                reverse_num = reverse_num * 10 + num

            if reverse_num == x_origin:
                return True
            else:
                return False


s = Solution()
print s.isPalindrome(10)
