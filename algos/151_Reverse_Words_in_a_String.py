class Solution:
    def reverseWords(self, s: str) -> str:
        
        # split the string into a list of strings 
        input_list = s.split(' ')
        
        # remove all of the empty strings from the list
        cleaned_list = [i for i in input_list if i != '']
        
        # reverse the list 
        cleaned_list.reverse()
        
        # join the reversed list back into a new string, separated by spaces 
        final_string = ' '.join(cleaned_list)
        
        return final_string
