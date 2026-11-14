class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1],reverse=True)
        ans=0
        for a,b in boxTypes:
            if truckSize>0:
                if a<=truckSize:
                    ans+= a*b
                    truckSize -=a
                else:
                    ans+=truckSize*b
                    truckSize = 0
        return ans
        