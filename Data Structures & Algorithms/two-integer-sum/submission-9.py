class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_hashmap = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in prev_hashmap:
                return [prev_hashmap[diff],i]
            prev_hashmap[n] = i

        return []
