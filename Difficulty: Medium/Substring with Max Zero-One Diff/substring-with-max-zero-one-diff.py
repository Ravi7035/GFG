class Solution:
	def maxSubstring(self, s):
		# code here
# 		if "0" not in s:
# 		    return -1
# 		maximum_diff=0
# 		for i in range(len(s)):
# 		    count1=0
# 		    count0=0
# 		    for j in range(i,len(s)):
# 		        if s[j]=="0":
# 		            count0+=1
# 		        else:
# 		            count1+=1
		            
#                 maximum_diff=max(maximum_diff,count0-count1)
            
#         return maximum_diff


        curr = 0
        best = float('-inf')

        for ch in s:
            val = 1 if ch == '0' else -1

            curr = max(val, curr + val)
            best = max(best, curr)

        return best if best > 0 else -1

        
		            
		
		        