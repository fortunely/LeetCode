class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = True
        single_sum = 0
        for i in range(len(digits) - 1, -1, -1):
            if carry:
                if digits[i] >= 9:
                    carry = True
                    digits[i] = digits[i] + 1 - 10

                    if i == 0:
                        digits.insert(0, 1)
                        break
                else:
                    carry = False
                    digits[i] = digits[i] + 1
                    break
            else:
                break

        return digits


s = Solution()

a = [1,2,3]
a = [4,9,9,9]
a1 = s.plusOne(a)

print a1

# b = [4,3,2,1]
# b1 = Solution(b)


