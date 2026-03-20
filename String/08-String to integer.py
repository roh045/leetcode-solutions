class Solution:
    def myAtoi(self, s):
        i, n = 0, len(s)
        sign = 1
        num = 0

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        
        while i < n and s[i] == ' ':
            i += 1

       
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

       
        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])

           
            if sign * num >= INT_MAX:
                return INT_MAX
            if sign * num <= INT_MIN:
                return INT_MIN

            i += 1

        return sign * num