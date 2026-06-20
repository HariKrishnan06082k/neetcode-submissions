class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        nums = [3,2,2,3] , val = 3 
        output = k = 2 , nums = [2,2,_,_]

        ''' 

        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
