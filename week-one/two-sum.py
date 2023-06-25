class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashMap: dict = dict()
        for i, val in enumerate(nums):
            if (target - val) in hashMap:
                return [i, hashMap[target - val]]
            else:
                hashMap[val] = i
        return []
