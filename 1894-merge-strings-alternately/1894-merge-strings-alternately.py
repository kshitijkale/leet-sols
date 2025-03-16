class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        count1 = 0
        count2 = 0
        sol =""
        while (count1 !=n1 and count2 != n2):
            count = count1+count2
            if(count%2==0):
                sol += word1[count1]
                count1+=1
            else:
                sol += word2[count2]
                count2+=1

        if(count1 == n1):
            for x in word2[count2:]:
                sol += x
        if(count2 ==  n2):
            for x in word1[count1:]:
                sol += x
        return sol