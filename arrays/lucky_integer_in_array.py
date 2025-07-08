from typing import List
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        n = len(arr)
        arr1 = []
        for i in range(n):
            k = arr[i]
            l = 0
            for j in range(n):
                if arr[j] == k:
                    l += 1
            if k == l and k not in arr1:
                arr1.append(k)
        n1 = len(arr1)
        if n1 == 0:
            return -1
        largest = arr1[0]
        for i in range(n1):
            if arr1[i] > largest:
                largest = arr1[i]
        return largest