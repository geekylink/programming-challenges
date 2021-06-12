class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(needle) == 0:
            return 0
        
        for i in range(0, len(haystack)):
            # No point in trying if it goes past the end of the haystack
            if i+len(needle) > len(haystack):
                break
            
            good = False
            subHay = haystack[i:i+len(needle)]
            if subHay == needle:
                return i
                
                
        return -1
