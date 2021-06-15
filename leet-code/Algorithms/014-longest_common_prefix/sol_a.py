class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        good = True
        index = 0
        
        if len(strs) == 0 or len(strs[0]) == 0:
            return ""
        
        while good:
            if index >= len(strs[0]):
                good = False
                break
                
            letter = strs[0][index]
            for word in strs:
                if index >= len(word):
                    good = False
                    break
                if word[index] != letter:
                    good = False 
            if good:
                index = index + 1
                
                
        return strs[0][:index]
                
