class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0 
        running_length = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                counter += 1 # 1 2 
                running_length = max(counter, running_length) # 2
                print("running length", running_length)
            if nums[i] == 0:
                counter = 0 
        return running_length

