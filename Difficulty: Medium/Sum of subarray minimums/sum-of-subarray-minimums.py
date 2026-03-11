class Solution:
    def sumSubMins(self, arr):
        # can solve this using monotic stack
        stack=[]
        output=0
        for i in range(len(arr)+1):
            while stack and (i==len(arr) or arr[stack[-1]]>arr[i]):
                j=stack.pop()
                k=stack[-1] if stack else -1
                output+=arr[j]*(i-j)*(j-k)
                
            stack.append(i)
            
        return output
            
            
            
            
        