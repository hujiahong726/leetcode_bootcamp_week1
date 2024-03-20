class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        lower = 2 ** 31
        upper = 2 ** 31 - 1
        s = s.strip()
        if not s:
            return 0
        i, num, sign = 0,0,1
        if s[0] == '+':
            sign = 1
            i += 1
        if s[0] == '-':
            sign = -1
            i += 1

        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            num = num * 10 + digit
            if sign == 1 and num >= upper:
                return upper
            if sign == -1 and num >= lower:
                return -1 * lower
            i += 1
        return sign * num
