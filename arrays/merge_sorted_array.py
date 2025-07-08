from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        numsu1 = nums1[:m]
        numsu2 = nums2[:n]
        numsu1 += numsu2
        numsu1.sort()
        for i in range(m+n):
            nums1[i] = numsu1[i]