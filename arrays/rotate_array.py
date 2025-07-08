from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        for _ in range(k):
            last = nums[-1]
            for i in range(n-1,0,-1):
                nums[i] = nums[i-1]
            nums[0] = last