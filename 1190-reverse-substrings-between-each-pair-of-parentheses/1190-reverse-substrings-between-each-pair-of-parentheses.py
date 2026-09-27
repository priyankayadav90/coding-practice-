class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        opened_stack = []
        pair = [0] * n
        
        for i, char in enumerate(s):
            if char == '(':
                opened_stack.append(i)
            elif char == ')':
                j = opened_stack.pop()
                pair[i] = j
                pair[j] = i
                
        
        res = []
        i = 0
        direction = 1  
        
        while i < n:
            if s[i] == '(' or s[i] == ')':
                i = pair[i]       
                direction = -direction  
            else:
                res.append(s[i])
            i += direction        
            
        return "".join(res)
