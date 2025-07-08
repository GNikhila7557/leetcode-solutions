from typing import List
class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        for i in range(n):
            if nums[i] > 0:
                k = nums[i]
                result.append(nums[(i+k) % n])
            elif nums[i] < 0:
                k = abs(nums[i])
                result.append(nums[(i+n-k) % n])
            else:
                result.append(nums[i])
        return result