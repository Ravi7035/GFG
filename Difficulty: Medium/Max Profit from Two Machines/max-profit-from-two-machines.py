class Solution:
    def maxProfit(self, x, y, a, b):
        n=len(a)
        tasks=[]
        
        
        for i in range(n):
            diff=abs(a[i]-b[i])
            tasks.append((diff,a[i],b[i]))
            
            
        tasks.sort(reverse=True)
        
        countA=0
        countB=0
        total_profit=0
        
        for difference,profitA,profitB in tasks:
            
            if profitA > profitB:
                
                if countA <x:
                    total_profit+=profitA
                    countA+=1
                    
                else:
                    total_profit+=profitB
                    countB+=1
                    
                    
            else:
                
                if countB<y:
                    total_profit+=profitB
                    countB+=1
                    
                else:
                    total_profit+=profitA
                    countA+=1
                    
        return total_profit
                    
                    
        
                
                
        
        
