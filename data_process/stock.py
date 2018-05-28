# -*- encoding: utf-8 -*-
# public class Solution {
#     public int maxProfit(int[] prices) {
#         int res = 0;
#         for (int i = 0; i < prices.length - 1; ++i) {
#             if (prices[i] < prices[i + 1]) {
#                 res += prices[i + 1] - prices[i];
#             }
#         }
#         return res;
#     }
# }

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                res = res + prices[i + 1] - prices[i]
        return res


if __name__ == '__main__':
    r = Solution().maxProfit(prices=[7, 1, 5, 3, 6, 4])
    print(r)
