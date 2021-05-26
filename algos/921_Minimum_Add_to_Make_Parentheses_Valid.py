class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # --- spencer's way: use 2 stacks ---
        open_stack = []
        close_stack = []
        
        for letter in s:
            if letter == '(':
                open_stack.append(letter)
            elif letter == ')' and len(open_stack) > 0:
                open_stack.pop()
            elif letter == ')' and len(open_stack) == 0:
                close_stack.append(letter)
                
        return (len(open_stack) + len(close_stack))
        
        
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # --- mike way: use 1 stack ---
        string_stack: list = []
            
        for letter in s:
            if len(string_stack) == 0: 
                # add the current letter to the top of the stack 
                string_stack.append(letter)
            elif letter==')' and string_stack[-1]=='(':
                # pop the top off the stack 
                string_stack.pop()
            else:
                # add the next letter to the stack 
                string_stack.append(letter)
        
        return len(string_stack)
