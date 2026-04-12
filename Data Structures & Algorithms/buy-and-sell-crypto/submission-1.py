class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        profit=-math.inf
        for i in range(n-1):
            for j in range(i,n):
                temp=prices[j]-prices[i]
                if temp>profit:
                    profit=temp
        return profit if n>1 else 0
