class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dic={}
        arr=[]
        nums = sorted(nums)
        for i in range(len(nums)):
            target = -1*nums[i]
            p1=i+1
            p2=len(nums)-1
            while p1<p2:
                temp = nums[p1] + nums[p2]
                if temp == target and p1!=i and p2!=i:
                    arr.append([nums[p1], nums[p2], nums[i]])
                if temp < target:
                    p1+=1
                else:
                    p2-=1
        print(arr)
        result = []
        for i in range(len(arr)):
            temp = sorted(arr[i])
            key = ','.join(str(num) for num in temp)
            if key not in dic:
                dic[key] = temp
                result.append(temp)
        return result