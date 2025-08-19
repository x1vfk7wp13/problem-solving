class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {"I": 1, "V": 5, "X" : 10, "L" : 50, "C": 100, "D":500, "M": 1000}
        total = 0
        i = 0
        while i < len(s):
            if i == len(s) - 1 or numerals[s[i]] >= numerals[s[i+1]]:
                total += numerals[s[i]]
                i += 1
            else:
                total += numerals[s[i+1]] - numerals[s[i]]
                i += 2
        return total
