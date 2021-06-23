class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        else:
            going_down = True
            letter_dict = {}
            row_num = 1

            for i, letter in enumerate(s):
                print(f'row_num: {row_num}')

                # create the number of lists we need in the values for each k-v pair 
                if i < numRows: 
                    letter_dict[row_num] = [s[i]]
                # then fill the values in with letters once the lists are made 
                else:
                    letter_dict[row_num].append(s[i])

                if going_down: 
                    row_num+=1  # we're going down!
                else: 
                    row_num-=1  # we're going back up!

                if row_num == numRows:
                    # reverse direction to go back up 
                    going_down = False

                if row_num == 1: 
                    # reverse direction to go back down 
                    going_down = True

            # make the final answer 
            answer = []
            for r, letter_list in letter_dict.items():
                print(r, letter_list)
                answer.extend(letter_list)

            return ''.join(answer) 
