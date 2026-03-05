class Solution:
    def longestKSubstr(self, s, k):
        #declaring hash map to track count of distinct ones
        freq={}
        i=0
        longest=-1
        for  j in range(len(s)):
            freq[s[j]]=freq.get(s[j],0)+1
            
            while len(freq)>k:
                freq[s[i]]-=1
                if freq[s[i]]==0:
                    del freq[s[i]]
                i+=1
                
            if len(freq)==k:
                longest=max(j-i+1,longest)
            
        return longest
                
            
            
            
            
        
        