class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        s1 = set("qwertyuiop")
        s2 = set("asdfghjkl")
        s3 = set("zxcvbnm")
        result_strings: list = []
        
        for word in words: 
            distinct_letters: set = set(word.lower())
                
            if distinct_letters.issubset(s1):
                result_strings.append(word)
            elif distinct_letters.issubset(s2):
                result_strings.append(word)
            elif distinct_letters.issubset(s3):
                result_strings.append(word)
                
        return result_strings
