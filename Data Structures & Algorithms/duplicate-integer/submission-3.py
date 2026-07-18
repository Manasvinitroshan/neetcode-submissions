class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        c = set()

        i = 0

        for i in nums:
            if i in c:
                return True
            
            else:
                c.add(i)

        return False
         