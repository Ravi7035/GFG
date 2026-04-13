class Solution:
    def nextPalindrome(self, num):
        n=len(num)
        
        palindrome=num[:]
        
        #special case if all nums are 9's
        
        if all(digit==9 for digit in num):
            
            return [1] +[0]*(n-1) + [1]
            
            
            
        
        mid=len(num)//2
        
        for i in range(n):
            palindrome[n-1-i]=palindrome[i]
            
        #check if the current palindrome is larger than the input
        
       
        
        if palindrome > num:
            
            return palindrome
            
        #adjust the mid and carry
        
        carry=1
        mid=n//2
        
        if n%2==1:
            
            palindrome[mid]=palindrome[mid]+1
            
            if palindrome[mid]==10:
                
                palindrome[mid]=0
                
                carry=1
                
            else:
                carry=0
                
            left=mid-1
            
        else:
            
            left=mid-1
            
        #carrying the carry to the left
        
        while left >=0 and carry:
            
            val=palindrome[left]+carry
            
            if val ==10:
                palindrome[left]=0
                carry=1
                
            else:
                palindrome[left]=val
                carry=0
                
                
            left-=1
            
        #again mirror the palindrome list
        
        for i in range(n):
            palindrome[n-i-1]=palindrome[i]
            
            
        return palindrome
            
            
            
            
            
            
        