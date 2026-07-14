class Solution:
    def find(self, arr):
        # code here
        need = 0

        for i in range(len(arr) - 1, -1, -1):
            need = (need + arr[i] + 1) // 2   # ceil((need+arr[i])/2)

        return need