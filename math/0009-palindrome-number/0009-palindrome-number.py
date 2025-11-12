class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        s = str(x)
        
        # Recursive helper function
        def helper(left, right):
            # Base case: all characters checked
            if left >= right:
                return True
            
            # Check current characters
            if s[left] != s[right]:
                return False
            
            # Recurse inward
            return helper(left + 1, right - 1)
        
        return helper(0, len(s) - 1)
        