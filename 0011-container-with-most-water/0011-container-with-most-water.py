class Solution:
    def maxArea(self, height: List[int]) -> int:
        # if i am getting closer and getting bigger then that value might give better volume
        l,r = 0,len(height)-1
        vol = 0
        # given 2 bards th vol is (l-r) * min(height[l],height[r])
        # therefore we might get better result using a taller value for the little homie 
        while l<r:
            if((r-l)*min(height[l],height[r])>vol):
                vol = (r-l)*min(height[l],height[r])

            if(height[l]<height[r]):
                l+=1
            else:
                r-=1
    
        return vol
            

        
        