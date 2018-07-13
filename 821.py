class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        indexes = [index for index, item in enumerate(S) if item == C]
        areas = [(-9999, indexes[0])]
        for i in range(len(indexes) - 1):
            areas.append((indexes[i], indexes[i+1]))
        areas.append((indexes[-1], 9999))
        result = []
        for index, item in enumerate(S):
            if item == C:
                result.append(0)
                continue
            for left, right in areas:
                if left <= index <= right:
                    result.append(min(index - left, right - index))
                    break
        return result


class Solution2:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        prev = float('-inf')
        result = []
        for index, item in enumerate(S):
            if item == C:
                result.append(0)
                prev = index
            else:
                result.append(index - prev)

        prev = float('inf')
        for index in range(len(S) - 1, -1, -1):
            if S[index] == C:
                prev = index
            else:
                result[index] = min(result[index], prev - index)

        return result


if __name__ == '__main__':
    print(Solution2().shortestToChar("loveleetcode", 'e'))
    print(Solution2().shortestToChar('baaa', 'b'))
    print(Solution2().shortestToChar('aaab', 'b'))
