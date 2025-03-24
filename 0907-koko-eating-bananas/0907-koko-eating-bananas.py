class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        res = hi
        while lo<=hi:
            k = (hi+lo)//2
            hm = 0
            for x in piles:
                hm += ceil(x/k)
            if hm<=h:
                res = min(res,k)  
                hi = k-1
            else:
                lo = k+1
        return res

