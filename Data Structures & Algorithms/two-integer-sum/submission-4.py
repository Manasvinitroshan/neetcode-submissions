class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        h1 = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in h1:
                return [h1[diff], i]
            h1[n] = i
        return




        
       

        
        