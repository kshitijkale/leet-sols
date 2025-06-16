class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1=len(word1)
        n2=len(word2)
        word = ""
        count1=0
        count2=0

        while count1!= n1 and count2!= n2:
            count = count1 + count2
            word += word1[count1]
            count1+=1
            word += word2[count2]
            count2+=1
        word = word +''.join(list(word1[count1:]))
        word = word +''.join(list(word2[count2:]))
        return word