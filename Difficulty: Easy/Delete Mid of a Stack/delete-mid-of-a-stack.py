class Solution:
    def deleteMid(self, stack):
        n = len(stack)
        middle_from_top = n - ((n + 1) // 2) + 1

        def deletemid(current):
            if not stack:
                return
            top = stack.pop()
            if current == middle_from_top:
                return 
            deletemid(current + 1)
            stack.append(top)
        
        deletemid(1) 
        return stack
            
            
          