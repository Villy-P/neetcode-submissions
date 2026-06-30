class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minim = prices[0]
        maxProfit = 0
        for i in prices:
            if i < minim:
                minim = i
            if i - minim > maxProfit:
                maxProfit = i - minim
        return maxProfit