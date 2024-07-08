class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        dictChar = Counter("".join(words))
        for key, value in dictChar.items():
            if value % len(words) != 0:
                return False
        return True