"""
给定一个正整数，返回它在 Excel 表中相对应的列名称。

例如，

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
示例 1:

输入: 1
输出: "A"
示例 2:

输入: 28
输出: "AB"
示例 3:

输入: 701
输出: "ZY"
"""

from string import ascii_uppercase
class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        lst = []
        dct = dict(enumerate(ascii_uppercase, start=1))

        while n:
            mod = n % 26
            n //= 26
            if mod == 0:
                mod = 26
                n -= 1
            lst.append(mod)

        return ''.join([dct[i] for i in reversed(lst)])
