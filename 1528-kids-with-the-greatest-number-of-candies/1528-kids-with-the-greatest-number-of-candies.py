class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest=0
        final = []
        for i in range(len(candies)):
            if (greatest<candies[i]):
                greatest = candies[i]
        for i in range(len(candies)):
            x = candies[i] + extraCandies
            if(x>=greatest):
                final.append(True)
            else:
                final.append(False)
        return final