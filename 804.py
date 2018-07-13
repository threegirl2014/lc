
class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morses = [".-","-...","-.-.","-..",".","..-.","--.",
                  "....","..",".---","-.-",".-..","--","-.",
                  "---",".--.","--.-",".-.","...","-","..-",
                  "...-",".--","-..-","-.--","--.."]
        lower_letters = 'abcdefghijklmnopqrstuvwxyz'
        letter2morse = {letter: morse for letter, morse in zip(lower_letters, morses)}
        translations = {''.join(morses[ord(letter) - ord('a')] for letter in word) for word in words}
#        translations = {''.join(letter2morse[letter] for letter in word) for word in words}
        return len(translations)


if __name__ == '__main__':
    solution = Solution()
    print(solution.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]) == 2)
