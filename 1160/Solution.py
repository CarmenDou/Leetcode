class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        sortedChars = sorted(chars)
        cnt = 0
        for word in words:
            sortedWord = sorted(word)
            i, j = 0, 0
            while i < len(sortedWord) and j < len(sortedChars):
                if sortedWord[i] == sortedChars[j]:
                    i += 1
                j += 1
            if i == len(sortedWord):
                cnt += i
        return cnt