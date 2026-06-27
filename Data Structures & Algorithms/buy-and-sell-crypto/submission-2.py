class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min=prices[0]
        profit=0
        for i in range(1, len(prices)):
            temp = prices[i] - min
            if temp > profit:
                profit = temp
            if min>prices[i]:
                min = prices[i]
        return profit