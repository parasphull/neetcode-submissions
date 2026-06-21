class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count +=1
            else:
                product = product * nums[i]
            if zero_count >1:
                product = 0
                break
    
        result = [0]*len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                result[i] = product
            else:
                if zero_count>0:
                    result[i] = 0
                else:
                    result[i] = product//nums[i]

        return result
        
