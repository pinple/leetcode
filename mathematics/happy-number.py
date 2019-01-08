"""
编写一个算法来判断一个数是不是“快乐数”。

一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。

示例: 

输入: 19
输出: true
解释: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        record = {}
        sq_sum = 0
        while n != 1:
          sq_sum = 0
          sub_num = n
          while sub_num > 0:
            sq_sum += (sub_num % 10) * (sub_num % 10)
            sub_num /= 10
          if sq_sum in record:
            return False
          else:
            record[sq_sum] = 1
          n = sq_sum
        return True