#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices) :
        if len(prices) == 0:
            return 0
        buy = prices[0]
        sell = 0
        profit = 0
        for i in range (1, len(prices)):
            if prices[i]<buy:
                buy= prices[i]
                sell=0
            else:
                sell = prices[i]
            profit = max(profit, sell- buy)
        return profit





if __name__ == '__main__':
        prices = [7,6,4,3,1]

        print(Solution().maxProfit(prices))