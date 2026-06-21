class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        result = 0
        for i in range(len(nums)):
            count = 1
            if nums[i] -1 not in numset:
                while (nums[i] + count) in numset:
                    count +=1
            result = max(count, result) 

        return result