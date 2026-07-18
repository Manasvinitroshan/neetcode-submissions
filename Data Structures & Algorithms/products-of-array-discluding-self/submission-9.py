class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        postfix = [1]*n
        prefix = [1]*n
        ans=[1]*n

        for i in range(1,n):
            prefix[i] = prefix[i-1]*nums[i-1]

        
        for j in range(n-2,-1,-1):
            postfix[j] = postfix[j+1]*nums[j+1]

        

        for a in range(n):
            ans[a] = prefix[a]*postfix[a]

        

        return ans



        