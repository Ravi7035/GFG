class Solution:
    def minMeetingRooms(self, start, end):
        # code here
        platforms=0
        max_platforms=0
        start.sort()
        end.sort()
        i=j=0
        while i < len(start):
            
            if start[i] < end[j]:
                i+=1
                platforms+=1
                max_platforms=max(platforms,max_platforms)
                
            else:
                platforms-=1
                j+=1
                
        return max_platforms
        
        
