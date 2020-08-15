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


ans = LongestPalindrome01()
print(ans.longestPalindrome("b"))
print(ans.longestPalindrome("xyzcbba"))
print(ans.longestPalindrome("b"))
print(ans.longestPalindrome("abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"))
