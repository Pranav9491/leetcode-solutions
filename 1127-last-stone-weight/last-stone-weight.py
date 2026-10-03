class Solution(object):
    def lastStoneWeight(self, stones):
        stones.sort(reverse=True)

        while len(stones) > 1:
            y = stones.pop(0)
            x = stones.pop(0)

            if y != x:
                stones.append(y - x)
                stones.sort(reverse=True)

        if stones:
            return stones[0]
        return 0