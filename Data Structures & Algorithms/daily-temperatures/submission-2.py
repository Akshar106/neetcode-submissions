class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0] * len(temperatures)
        left = 0

        for left in range(len(temperatures)):
            cnt = left + 1
            while cnt < len(temperatures) and temperatures[cnt] <= temperatures[left]:
                cnt += 1 
            
            
            if cnt < len(temperatures):
                stack[left] = (cnt - left)
        
        return stack
