class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        operation = ['+','D','C']
        scores = []
        for item in operations:
            if item not in operation:
                scores.append(int(item))
            else:
                if item == operation[0]:
                    scores.append(scores[-1]+scores[-2])
                elif item == operation[1]:
                    scores.append(scores[-1]*2)
                elif item == operation[2]:
                    scores.pop(-1)
        return sum(scores)

        