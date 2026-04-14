class Solution(object):
    def countPrefixes(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        c=0
        for i in words:
            n=len(i)
            if s[:n]==i and i in s:
                c+=1
        return c