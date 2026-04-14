class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        a=sentence.split()
        n=len(searchWord)
        for i in range(len(a)):
            if searchWord in a[i] and searchWord==a[i][0:n]:
                return i+1
        return -1
