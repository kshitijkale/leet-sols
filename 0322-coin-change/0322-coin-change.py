class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        amount 12
        0 1 2 3 4 5 6 7 8 9 10 11 12 # index
        0 1 2 3 4 1 2 3 4 5 1   2  3 # how many coins u will need
        dry running
        for 2 
        min coins if used one of the dj coins ==> can use 1 to make a 2 ==> now 1 is left which is made using 1 coin ==> 
        min{A[2-1]}+1
        then for 3 
        min{[A[3-1]]}+1
        and so on 
        for 5 
        its min{A[5-1],A[5-5]} + 1 ==> make 5 by choosing the coin 1 therefore now u need to make 4 in min way or make 5 by choosing 5 now u need to make 0in min way
        and the min of this or is choose 5 
        a[0] = 0
        a[1] = 1
        for i in 0 to 12:
            A[i] = min for all j coins st i - dj >= 0 { A[i-dj] }  + 1
        
        '''


        A = [0] * (amount+1)
        for i in range(1,amount+1):  # 0 to amount
            k = 0
            temp = float('inf')
            while k < len(coins):
                if(i-coins[k]>=0) and (A[i - coins[k]]<temp):
                    temp = A[i - coins[k]]
                k+=1
            A[i] = temp + 1
        return A[amount] if A[amount]!=float('inf') else -1
