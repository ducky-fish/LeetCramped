from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomLetters = sorted(Counter(ransomNote).items())
        for letters in ransomLetters:
            print(letters)
            
            if magazine.count(letters[0]) < letters[1]:
                return False
            
        return True
