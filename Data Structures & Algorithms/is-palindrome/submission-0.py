class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0
        

        result = ''.join(char.lower() for char in s if char.isalnum())
        right = len(result) - 1
        print(result)


        while left < right:
            if(result[left] != result[right]):
                return False
            else:
                left+=1
                right-=1

    
        return True
 
        