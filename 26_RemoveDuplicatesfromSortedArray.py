class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if None == nums or 0 == len(nums):
            return 0

        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[j - 1]:
                nums[j] = nums[i]
                j += 1
            else:
                pass

        return j


# nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,4]
s = Solution()

print s.removeDuplicates(nums)
print nums