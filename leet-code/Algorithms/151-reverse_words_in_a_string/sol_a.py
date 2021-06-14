#!/bin/python3
class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        words = s.split(" ")
        
        for i in range(1, len(words) + 1):
            if words[-1*i] == "":
                continue
            res = res + " " + words[-1*i]
            
        # Remove the leading character
        return res[1:]
