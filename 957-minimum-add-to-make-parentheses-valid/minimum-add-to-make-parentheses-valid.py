class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        remaining=0
        count=0
        for ch in s:
            if ch == '(':
                remaining +=1
            else:
                if remaining>0:
                    remaining-=1
                else:
                     count +=1
        return count+remaining

        