class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        esc = "'.,:;/?!@#$%^&*( )\"\_-+=[]{}<>~`"
        
        for ch in esc:
            s = s.replace(ch, "")
            print(ch)
            
        s = s.lower()
        
        l = 0
        r = len(s) - 1
        
        while (l < r and l != r):
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
            
        return True