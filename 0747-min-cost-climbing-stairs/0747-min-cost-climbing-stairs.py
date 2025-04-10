class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        i start with the last stair
        i came to n from either n-1 or n-2
        cost to come from n-1 is mincost[n-1]+cost[n]
        cost to come from n-2 is mincost[n-2]+cost[n]

        so min cost to get to n is 
                    mincost[n] = min{mincost[n-1],mincost[n-2]} + 1

        '''
        n = len(cost)
        mincost = [0] * (n+1)
        mincost[0] = 0
        mincost[1] = 0
        for i in range(2,n+1):
            mincost[i] = min(mincost[i-1]+cost[i-1],mincost[i-2]+cost[i-2])

        return mincost[n]



