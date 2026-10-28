class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        mc1, mc2 = cost[0], cost[1]

        for c in cost[2:]:
            temp = min(c+mc1, c+mc2)
            mc1 = mc2
            mc2 = temp

        return mc2