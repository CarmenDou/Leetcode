class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score, curScore = 0, 0
        tokens.sort()
        i, j = 0, len(tokens)-1
        while i <= j:
            if tokens[i] <= power:
                curScore += 1
                score = max(score, curScore)
                power -= tokens[i]
                i += 1
            else:
                if curScore <= 0:
                    break
                curScore -= 1
                score = max(score, curScore)
                power += tokens[j]
                j -= 1
        return score
        

