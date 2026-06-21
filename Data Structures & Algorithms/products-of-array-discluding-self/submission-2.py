class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_arr = [1]*len(nums)
        suffix_arr = [1]*len(nums)
        prefix_arr[1] = nums[0]
        suffix_arr[len(nums)-2] = nums[len(nums)-1]
        for i in range(2, len(nums)):
            prefix_arr[i] = nums[i-1]*prefix_arr[i-1]
            suffix_arr[len(nums) - i-1] = nums[len(nums) - i]* suffix_arr[len(nums) - i]
        

        return [prefix_arr[i]*suffix_arr[i] for i in range(len(nums))]
        
