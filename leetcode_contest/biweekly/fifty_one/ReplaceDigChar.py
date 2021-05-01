# https://leetcode.com/contest/biweekly-contest-51/problems/replace-all-digits-with-characters/

class ReplaceDigChar:

    def replaceDigits(self, s):        
        n = len(s)
        for i in range(1, n, 2):
            new_chr = self.shift(s[i-1], int(s[i])) 
            s = s[:i] + new_chr + s[i+1:]
        return s
            
            
    
    def shift(self, a, num):
        return chr(ord(a)+num)
    