class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        tmp = [0, 0, 0]
        for triplet in triplets:
            aMax = max(tmp[0], triplet[0])
            bMax = max(tmp[1], triplet[1])
            cMax = max(tmp[2], triplet[2])
            if aMax <= target[0] and bMax <= target[1] and cMax <= target[2]:
                tmp = [aMax, bMax, cMax]
                if tmp == target:
                    return True
        
        return tmp == target