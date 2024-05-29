from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()

        for n in nums:
            if n in hashSet:
                return True
            hashSet.add(n)

        return False
    
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        characterMapS, characterMapT = {}, {}

        for i in range(len(s)):
            characterMapS[s[i]] = characterMapS.get(s[i], 0) + 1
            characterMapT[t[i]] = characterMapT.get(t[i], 0) + 1

        return characterMapS == characterMapT
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]

        remainderMap = {} # remainder -> index

        for index, value in enumerate(nums):
            remainder = target - value

            if remainder in remainderMap:
                return [remainderMap[remainder], index]

            remainderMap[value] = index
