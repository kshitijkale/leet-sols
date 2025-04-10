class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        ways i can reach nth place is eiether i took a 1 jump or a 2 jump to it.
        so climbstairs[n] = climbstairs[n-1]+climbstair[n-2]]

        so i can call this reccurently from the top down == > cs[n] ==> cs[n-1](-->cs[n-2] and --> cs[n-3]) and cd[n-2](-->cs[n-3] and -->cs[n-4] and so on)

        or i can go bottum up and store values in an array.
        '''

        D = []
        D.append(1)
        D.append(2)
        for i in range(2,n):
            D.append(D[i-1]+D[i-2])

        return D[n-1]

         