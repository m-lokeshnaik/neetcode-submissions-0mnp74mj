class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        if n<=1:
            return 0
        min_price=prices[0]
        max_profit=0
        for price in prices[1:]:
            profit=price-min_price
            max_profit=max(max_profit,profit)
            min_price=min(min_price,price)
        return max_profit

        #-----------brute force --------------
        # profit=-math.inf
        # for i in range(n-1):
        #     for j in range(i,n):
        #         temp=prices[j]-prices[i]
        #         if temp>profit:
        #             profit=temp
        # return profit if n>1 else 0
