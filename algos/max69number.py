class Solution:
    def maximum69Number (self, num: int) -> int:
        string_num = str(num)
        nine_flag = 0
        new_string_num = []
        
        for string_digit in string_num:
            # we only want to change the FIRST 6 we find
            if nine_flag == 0:
                # if the digit is a 6, then we add a nine instead
                if string_digit != '9':
                    new_string_num.append('9')
                    nine_flag += 1
                else:
                    new_string_num.append(string_digit)
            else:
                new_string_num.append(string_digit)

        # join the strings in the list with an empty string delimiter
        solution = ''.join(new_string_num)

        return int(solution)


class BetterSolution:
    def maximum69Number (self, num: int) -> int:
        return int(str(num).replace('6', '9', 1))


"""
The lesson here is to use the str.replace method whenever possible! 
Remember that str.replace() can be used with an optional 'count' value 
specifying the number of old values that you want to replace. If count 
is 1, then the str.replace() method call will only replace the first
occurrence of the string to be replaced. (As is the case in this example) 
"""