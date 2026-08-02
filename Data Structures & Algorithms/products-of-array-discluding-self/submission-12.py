class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        pre = [1]*n
        post = [1]*n
        ans = [1]*n

        for i in range(1,n):
            pre[i] = pre[i-1] * nums[i-1]
        
        print(pre)

        for j in range(n-1,0,-1):
            
            post[j-1] = post[j]*nums[j]
           

        print(post)
        
        for a in range(n):
            ans[a] = pre[a]*post[a]


        return ans
        