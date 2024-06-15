class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        coins.sort()
        bCoins = [False] * (amount+1)
        comAmount = [float('inf')] * (amount+1)

        for coin in coins:
            if coin < amount+1:
                bCoins[coin] = True
                comAmount[coin] = 1

        i = 1
        while i < amount+1:
            if bCoins[i]:
                for coin in coins:
                    if coin+i < amount+1:
                        bCoins[coin+i] = True
                        comAmount[coin+i] = min(comAmount[coin+i], comAmount[i]+1)
            i += 1
        
        return comAmount[amount] if comAmount[amount] != float('inf') else -1