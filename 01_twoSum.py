class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {} # storage difference . Key = difference, Value = index of value in  List nums
        i = 0
        while i < len(nums):
            differ = target - nums[i]
            differ_str = str(differ)

            if str(nums[i]) in dict.keys():
                return [dict[str(nums[i])], i]
            else:
                dict[differ_str] = i

            i += 1

        return []


nums = [2, 7, 11, 15]
s = Solution()
results = s.twoSum(nums, 9)
print results