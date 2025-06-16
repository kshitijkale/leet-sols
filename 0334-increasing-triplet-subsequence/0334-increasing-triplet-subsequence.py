class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        #LINEAR SOLUTION EXPECTED 
        # what i want to do is when i find a number if it is smaller num 1 put it there given num 2 not chosen

        n1 = float('inf')
        n2 = float('inf')

        for num in nums:
            if num<=n1:
                n1=num
            elif num<= n2:
                n2=num
            else:
                return True
        return False