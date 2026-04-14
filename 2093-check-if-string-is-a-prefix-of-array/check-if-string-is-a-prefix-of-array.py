class Solution:
    def isPrefixString(self, s: str, words: list[str]) -> bool:
        prefix = ""
        for word in words:
            prefix += word
            
            # If we find an exact match, it's a prefix string
            if prefix == s:
                return True
            
            # If the prefix length exceeds s, we can stop early
            if len(prefix) > len(s):
                return False
                
        return False