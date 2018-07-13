class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        s1 = 'qwertyuiop'
        s2 = 'asdfghjkl'
        s3 = 'zxcvbnm'
        result = []
        for word in words:
            lword = word.lower()
            if all(c in s1 for c in lword) or all(c in s2 for c in lword) or all(c in s3 for c in lword):
                result.append(word)
        return result


class Solution2:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        s1 = set('qwertyuiop')
        s2 = set('asdfghjkl')
        s3 = set('zxcvbnm')
        result = []
        for word in words:
            lword = set(word.lower())
            if lword.issubset(s1) or lword.issubset(s2) or lword.issubset(s3):
                result.append(word)
        return result
