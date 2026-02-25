class Solution:
    def sortStack(self, st):
        # code here 
        def Insertsort(st,element):
            if not st or st[-1] <= element:
                st.append(element)
                return
            temp=st.pop()
            Insertsort(st,element)
            st.append(temp)
        
        def sortedstack(st):
            if not st:
                return 
            temp=st.pop()
            sortedstack(st)
            Insertsort(st,temp)
            
        sortedstack(st)
        
        return st