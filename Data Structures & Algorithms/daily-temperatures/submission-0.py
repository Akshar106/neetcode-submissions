class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0] * len(temperatures)
        start = 0

        for start in range(len(temperatures)):
            cnt = start + 1
            while cnt < len(temperatures) and temperatures[cnt] <= temperatures[start]:
                cnt += 1
            
            if cnt < len(temperatures):
                stack[start] = cnt - start
                
        return stack
