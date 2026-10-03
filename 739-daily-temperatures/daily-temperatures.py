class Solution(object):
    def dailyTemperatures(self, temperatures):
         s=[]
         n=len(temperatures)
         ans=[0]*n
         for i,t in enumerate(temperatures):
            while s and t>s[-1][0]:
                st,si=s.pop()
                d=i-si
                ans[si]=d
            s.append([t,i])
         return ans

         
        