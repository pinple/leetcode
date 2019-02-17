"""
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
"""

import random


class Solution(object):
  def findKthLargest(self, nums, k):
    """
    :type A: List[int]
    :type k: int
    :rtype: int
    """

    def quickselect(start, end, nums, k):
      if start == end:
        return nums[start]

      mid = partition(start, end, nums)

      if mid == k:
        return nums[mid]
      elif k > mid:
        return quickselect(mid + 1, end, nums, k)
      else:
        return quickselect(start, mid - 1, nums, k)

    def partition(start, end, nums):
      p = random.randrange(start, end + 1)
      pv = nums[p]
      nums[end], nums[p] = nums[p], nums[end]
      mid = start
      for i in range(start, end):
        if nums[i] >= pv:
          nums[i], nums[mid] = nums[mid], nums[i]
          mid += 1
      nums[mid], nums[end] = nums[end], nums[mid]
      return mid

    ret = quickselect(0, len(nums) - 1, nums, k - 1)
    return ret

  def partition(start, end, nums):
    p = random.randrange(start, end + 1)
    pv = nums[p]
    nums[end], nums[p] = nums[p], nums[end]
    mid = start
    for i in range(start, end):
      if nums[i] >= pv:
        nums[i], nums[mid] = nums[mid], nums[i]
        mid += 1
    nums[mid], nums[end] = nums[end], nums[mid]
    return mid