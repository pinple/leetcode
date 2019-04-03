"""
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

示例 1:

输入: nums = [1,2,3,1], k = 3
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1
输出: true
示例 3:

输入: nums = [1,2,3,1,2,3], k = 2
输出: false
"""
from collections import deque


class Solution(object):
  def containsNearbyDuplicate(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    if not nums:
      return False
    if k == 0:
      return False
    k = k + 1
    k = min(k, len(nums))

    window = deque([])
    d = set()
    for i in range(0, k):
      if nums[i] in d:
        return True
      d |= {nums[i]}
      window.append(i)
    for i in range(k, len(nums)):
      d -= {nums[window.popleft()]}
      if nums[i] in d:
        return True
      d |= {nums[i]}
      window.append(i)
    return False
