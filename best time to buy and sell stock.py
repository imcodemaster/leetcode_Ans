#creating class

class Solution:
    def maxProfit(self, prices):
        max_profit, min_price = 0, float("inf")
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)  
        return max_profit

if __name__ == "__main__":
    result = Solution().maxProfit([4,6,2,5,2,7,3])
    print (result)


#task completed
    
