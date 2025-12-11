class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()            # remove extra spaces
        last_word = s.split()[-1]  # get last word
        return len(last_word)
