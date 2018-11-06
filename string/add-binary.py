"""
给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"
"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        diff = abs(len(a) - len(b))
        if len(a) > len(b):
            b = "0" * diff + b
        else:
            a = "0" * diff + a
            
        ret = ""
        carry = 0
        ai, bi = len(a) - 1, len(b) - 1
        al, bl = len(a), len(b)
        while ai >= 0 and bi >= 0:
            ac, bc = a[ai], b[bi]
            if ac == "1" and bc == "1":
                if carry == 1:
                    ret += "1"
                else:
                    ret += "0"
                carry = 1
            elif ac == "0" and bc == "0":
                if carry == 1:
                    ret += "1"
                else:
                    ret += "0"
                carry = 0
            else:
                if carry == 1:
                    ret += "0"
                else:
                    ret += "1"

            ai -= 1
            bi -= 1

        if carry == 1:
            ret += "1"
        return ret[::-1]
