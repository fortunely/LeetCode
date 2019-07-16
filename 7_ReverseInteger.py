import math
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0

        # judge and keep sign, let x keep positive
        if x >= 0:
            positiveSign = True
        else:
            positiveSign = False
            x = -x

        # get the number one by one
        while 0 != x:
            num = x % 10
            x = x / 10

            result = result * 10 + num

        # add the sign
        if not positiveSign:
            result = -result

        # overflow check
        # maxPower = math.pow(2,31)
        maxPower = 1 << 31
        minNum = -maxPower
        maxNum = maxPower - 1
        if result >= minNum and result <= maxNum:
            return result
        else:
            return 0


s = Solution()
print s.reverse(9646324351)