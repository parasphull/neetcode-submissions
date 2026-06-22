class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1=0
        p2=1
        while p2<len(numbers):
            sum = numbers[p1] + numbers[p2]
            if sum == target:
                return [p1+1, p2+1]
            elif sum < target:
                p1 += 1
                p2 += 1
            else:
                p1 -=1
