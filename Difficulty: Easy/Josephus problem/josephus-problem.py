class Solution:
    def josephus(self, n, k):
        """
        ans=0
        for i in range(2,n+1):
            ans=(ans+k)%i
        return ans+1
        """
        def josephus(n,k):
            
            if n==1:
                return 0
               
            return (josephus(n-1,k)+k)%n
            
        return josephus(n,k)+1

            
       