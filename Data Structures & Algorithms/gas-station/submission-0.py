class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1

        start = 0
        gas_reserve = 0
        for i in range(len(gas)):
            gas_reserve+=gas[i]
            if cost[i]>gas_reserve:
                start = i+1
                gas_reserve = 0
            else:
                gas_reserve-=cost[i]

        return start