class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_c =  max(candies)
        return [(i+extraCandies >= max_c) for i in candies]