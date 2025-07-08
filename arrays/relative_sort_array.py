from collections import Counter
from typing import List
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = Counter(arr1)
        result = []
        for num in arr2:
            result.extend([num] * freq[num])
            freq[num] = 0
        remaining = []
        for num in freq:
            remaining.extend([num] * freq[num])
        result += sorted(remaining)
        return result