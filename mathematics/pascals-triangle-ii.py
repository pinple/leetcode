"""
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 3
输出: [1,3,3,1]
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        fact = [1] * (rowIndex + 1)
        ans = [1] * (rowIndex + 1)
        for i in range(1, rowIndex + 1):
            fact[i] = fact[i - 1] * i
        for i in range(1, rowIndex):
            ans[i] = fact[rowIndex] / (fact[i] * fact[rowIndex - i])
        return ans

"""
分析：

第k列数组的值其实就是二项式系数，按照公式C(n,k)实现即可
"""