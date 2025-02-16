class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans_instance = []
        res = []
        def back_track(openN , closeN):
            if openN == closeN == n:
                res.append("".join(ans_instance))

            if openN<n:
                ans_instance.append("(")
                back_track(openN+1,closeN)
                ans_instance.pop() 
            
            if closeN<openN:
                ans_instance.append(")")
                back_track(openN,closeN+1)
                ans_instance.pop()
        back_track(0,0)
        return res