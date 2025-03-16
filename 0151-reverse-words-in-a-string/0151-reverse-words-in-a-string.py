class Solution:
    def reverseWords(self, s: str) -> str:
        sol = []
        i = 0
        n = len(s)

        while i < n:
            # Skip leading spaces
            while i < n and s[i] == ' ':
                i += 1
            if i >= n:
                break  # If we reach the end, stop

            # Extract a word
            temp = ""
            while i < n and s[i] != ' ':
                temp += s[i]
                i += 1

            # Add the word to the list
            sol.append(temp)

        # Reverse the list and join with spaces
        return ' '.join(sol[::-1])


            
                

        