class Solution:
    def checkElements(self, start, end, arr):
        # code here
        ans=True
        for i in range(start,end+1):

            if i in arr:
                continue
            ans=False
            break

        return ans
