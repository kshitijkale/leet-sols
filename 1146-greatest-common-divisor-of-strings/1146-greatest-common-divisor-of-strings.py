class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)
        def isdivisor(l):
            if len1%l or len2%l:
                return False
            can = min(str1,str2)
            m1,m2 = len1//l , len2//l
            return can[:l]*m1 == str1 and can[:l]*m2 == str2
        for l in range(min(len1,len2),0,-1):
            if(isdivisor(l)):
                return str1[:l]
        return ""