class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        rev = 0
        while temp > 0:
            remainder = temp % 10
            rev = rev * 10 + remainder
            temp = temp // 10
        if rev == x:
            return True
        else:
            return False


        