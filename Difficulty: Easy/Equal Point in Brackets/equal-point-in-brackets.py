class Solution:
    def findIndex(self, s):
        # code here 
        total_close=s.count(")")
        open_count=0
        close_count = 0

        for i in range(len(s) + 1):

            if open_count == total_close - close_count:
                return i
            if i < len(s):
            
                if s[i] == '(':
                    open_count += 1
                else:
                    close_count += 1

        return len(s)
