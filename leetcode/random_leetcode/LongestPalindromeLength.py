import json
import os

'''
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3423/

'''


class LongestPalindromeLength:

    def longestPalindrome(self, s: str) -> int:
        char_dict = {}
        n = len(s)
        for i in range(n):
            if(s[i] in char_dict):
                char_dict[s[i]] = char_dict[s[i]] + 1
            else:
                char_dict[s[i]] = 1
        odd_count = 0
        even_count = 0
        for key in char_dict.keys():
            curr_val = char_dict[key]
            if(odd_count == 0 and curr_val % 2 != 0):
                odd_count = 1
                even_count += curr_val-1
            elif(curr_val % 2 != 0):
                even_count += curr_val-1
            else:
                even_count += curr_val
        return even_count + odd_count


ans = LongestPalindromeLength()
print(ans.longestPalindrome('abccccdd'))
