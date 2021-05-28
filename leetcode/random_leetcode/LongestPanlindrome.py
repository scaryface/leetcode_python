import json
import os

'''
https://leetcode.com/problems/longest-palindromic-substring/

'''


class LongestPalindrome01:

    def longestPalindrome(self, s: str) -> str:
        max_palin = ''
        is_palin = [[False for x in range(len(s))] for x in range(len(s))]
        for x in range(len(s)):
            for y in range(len(s)):
                if(y < x):
                    is_palin[x][y] = is_palin[y][x]
                else:
                    is_palin[x][y] = LongestPalindrome01.check_palin(
                        self, s, x, y)
                    if(is_palin[x][y] and len(max_palin) < y-x+1):
                        max_palin = s[x:y+1]
        return max_palin

    def check_palin(self, s: str, start: int, end: int) -> bool:
        while(start <= end):
            if(s[start] != s[end]):
                return False
            start = start + 1
            end = end - 1
        return True


class LongestPalindrome02:

    def longestPalindrome(self, s: str) -> str:
        reverse_s = LongestPalindrome02.reverse_str(self, s)
        n = len(s)
        max_palin = ''
        for i in range(n):
            if(s[i] == reverse_s[-i]):
                left_index = i
                while(i < n and s[i] == reverse_s[i]):
                    i = i+1
                curr_max = s[left_index:i+1]
                if(len(curr_max) > len(max_palin)):
                    max_palin = curr_max
        return max_palin

    def reverse_str(self, s: str) -> str:
        reverse_s = ''
        n = len(s)
        for i in range(n):
            reverse_s = reverse_s + s[-(i+1)]
        return reverse_s


# ans = LongestPalindrome01()
# print(ans.longestPalindrome("b"))
# print(ans.longestPalindrome("xyzcbba"))
# print(ans.longestPalindrome("b"))


# f = open(os.getcwd() + "/test_cases/test_cases.json")
# data = json.load(f)
# args = data["LongestPalindrome"]
# for element in args:
#     print(ans.longestPalindrome(args[element][0]))

print()
ans = LongestPalindrome02()
print(ans.longestPalindrome("b"))
print(ans.longestPalindrome("xyzcbba"))
print(ans.longestPalindrome("b"))
