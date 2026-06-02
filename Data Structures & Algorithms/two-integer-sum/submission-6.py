class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        final_list = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    if i<j:
                        final_list.append(i)
                        final_list.append(j)
                    else:
                        final_list.append(j)
                        final_list.append(i)
                    return final_list
