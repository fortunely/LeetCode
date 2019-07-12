class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i , j in enumerate(numbers):
            idx = i + 1 # calibrate the index
            if str(j) in dict.keys():
                return [dict[str(j)], idx]  # find out the first result
            else:
                dict[str(target - j)] = idx

        # not found
        return [0, 0]


numbers = [2, 7, 11, 15]
target = 9
s = Solution()
print s.twoSum(numbers, target)