class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = prices[0]
        max_ = 0
        for i in range(1,len(prices)):
            if(prices[i]<buy):
                buy = prices[i]
            else:
                max_ = max(prices[i] - buy,max_)
        return max_




