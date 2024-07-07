class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        visitedFrom = set()
        viistedTo = set()
        for cityFrom, cityTo in paths:
            if cityFrom not in viistedTo:
                visitedFrom.add(cityFrom)
            else:
                viistedTo.remove(cityFrom)
            if cityTo not in visitedFrom:
                viistedTo.add(cityTo)
            else:
                visitedFrom.remove(cityTo)
        for to in viistedTo:
            return to
        