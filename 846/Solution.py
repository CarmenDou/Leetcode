class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        while hand:
            preNum, i = hand[0]-1, 1
            while i <= groupSize:
                if preNum+1 in hand:
                    hand.remove(preNum+1)
                    preNum += 1
                else:
                    return False
                i += 1
        return True