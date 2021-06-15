class Solution:
    def addBinary(self, a: str, b: str) -> str:
        iA, iB = 0, 0
        
        for i in range(0,len(a)):
            if a[i] == "1":
                iA += 2**(len(a)-1-i)
        
        for i in range(0,len(b)):
            if b[i] == "1":
                iB += 2**(len(b)-1-i)
                
        return str(bin(iA+iB))[2:]
