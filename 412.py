class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in range(1, n + 1):
            temp1 = i % 3
            temp2 = i % 5
            if not temp1 and not temp2:
                result.append('FizzBuzz')
            elif not temp1:
                result.append('Fizz')
            elif not temp2:
                result.append('Buzz')
            else:
                result.append(str(i))
        return result
