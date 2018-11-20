"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。

在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = [[1] * n for n in xrange(1, numRows + 1)]
        for i in range(3, numRows + 1):
            for j in range(0, i - 2):
                ans[i - 1][1 + j] = ans[i - 2][j] + ans[i - 2][j + 1]
        return ans