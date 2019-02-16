"""
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
"""

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(n, dp):
          for i in range(2, n):
            if dp[i] == 1:
              k = i * i
              if k >= n:
                return
              while k < n:
                dp[k] = 0
                k += i

        if n < 2:
          return 0
        ans = 0
        dp = [1] * n
        dp[0] = 0
        dp[1] = 0
        helper(n, dp)
        # for i in range(0, n):
        #     if dp[i] == 1:
        #         print i + 1

        return sum(dp)
