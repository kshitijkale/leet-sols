class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = prices[0]
        max_ = 0
        i = 0
        while i<len(prices):
            if(prices[i]<buy):
                buy = prices[i]
            else:
                max_ = max(prices[i] - buy,max_)
            i+=1
        return max_




