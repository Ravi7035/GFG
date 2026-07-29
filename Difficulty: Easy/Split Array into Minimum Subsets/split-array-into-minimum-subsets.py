class Solution:
    def minSubsets(self, arr):
        #code here
        arr.sort()
        groups=1
        for i in range(1,len(arr)):
            
            if arr[i] != arr[i-1]+1:
                groups+=1
        return groups
                