class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        diff = 0
        buy = prices[0]

        for i in range(1, len(prices)):
            diff = prices[i] - buy

            if prices[i] < buy:
                buy = prices[i]
            
            elif diff > profit:
                profit = max(profit, diff)
        
        return profit
        