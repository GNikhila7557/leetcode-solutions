from typing import List
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n1 = []
        n2 = []
        result = []
        m = len(nums)
        for i in range(n):
            n1.append(nums[i])
        for i in range(n,m):
            n2.append(nums[i])
        for i in range(n):
            result.append(n1[i])
            result.append(n2[i])
        return result