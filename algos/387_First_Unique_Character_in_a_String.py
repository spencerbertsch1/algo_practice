class Solution:
    def firstUniqChar(self, s: str) -> int:
        letterDict = {}
        letters_seen_before: set = set()
        answer=-1

        # create the dictionary we will use for lookups 
        for letter in s:
            if letter in letters_seen_before:
                letterDict[letter]+=1
            else:
                 letterDict[letter] = 1
            letters_seen_before.add(letter)

        # iterate through the dict and find the first non-repeating letter
        first_unique_letter = ''
        for k, v in letterDict.items():
            print(f'letter:{k}, num_occurrences:{v}')
            if v == 1:
                first_unique_letter = k
                break
            
        # find the index of the first unique letter in the original string 
        if first_unique_letter != '':
            for i, letter in enumerate(s):
                if letter == first_unique_letter:
                    answer = i 
        
        return answer
