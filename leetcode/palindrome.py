class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = ''
        for i in range(0,len(s)):
            if (ord('a') <= ord(s[i].lower()) <= ord('z')) or ( ord('0') <= ord(s[i].lower()) <= ord('9'))
                clean_str += s[i].lower()

        return clean_str == clean_str[::-1]