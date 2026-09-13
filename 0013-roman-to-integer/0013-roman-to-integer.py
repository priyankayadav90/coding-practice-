class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        for current_char, next_char in zip(s, s[1:]):
            if roman_map[current_char] < roman_map[next_char]:
                total -= roman_map[current_char]
            else:
                total += roman_map[current_char]
        return total + roman_map[s[-1]]
