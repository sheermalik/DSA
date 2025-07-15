class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left,right=0,1
        bestProfit=0

        while right<len(prices):
            if prices[left] < prices[right]:
                profit= prices[right]-prices[left]
                bestProfit= max(bestProfit, profit)

            else:
                left= right  #doing left +=1 will not work 
            right+=1
        return bestProfit    

