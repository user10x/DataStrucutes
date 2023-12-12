class Solution(object):

    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        def digit(s):
            return ord(s) - ord('0')

        s = s.strip(' ')

        if s == "":
            return 0

        negative = False

        num = 0

        if s[0] == '-':
            negative = True
        elif s[0] == '+':
            negative = False
        elif 0 <= digit(s[0]) <= 9:
            num = digit(s[0])
        else:
            return num

        for i in range(1, len(s)):
            if 0 <= digit(s[i]) <= 9:
                num = num * 10 + digit(s[i])
            else:
                break

        if negative:
            if -num <= -2147483648:
                return -2147483648
            return -num
        else:
            if num >= 2147483647:
                num = 2147483647

            return num