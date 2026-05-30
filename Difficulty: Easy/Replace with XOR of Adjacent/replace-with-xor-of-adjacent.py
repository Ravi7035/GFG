class Solution:
    def replaceElements(self, arr):
        # code here
        n=len(arr)
        temp=[]
        for i in range(n):
            if i==0:
                temp.append(arr[0]^arr[1])
            elif i==n-1:
                temp.append(arr[n-2]^arr[n-1])
            else:
                temp.append(arr[i-1]^arr[i+1])
                
        for i in range(n):
            arr[i]=temp[i]
            
        
    
        