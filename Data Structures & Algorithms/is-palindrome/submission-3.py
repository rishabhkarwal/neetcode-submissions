LETTERS = {l for l in 'abcdefghijklmnopqrstuvwxyz'}
NUMBERS = {str(n) for n in range(10)}

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([character for character in s.lower() if character in LETTERS | NUMBERS])
        l, r = 0, len(s) - 1
        print(s)
        while l < r:
            left, right = s[l], s[r]
            if left != right: return False
            l += 1
            r -= 1
        return True