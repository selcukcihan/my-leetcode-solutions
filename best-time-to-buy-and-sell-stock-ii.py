from typing import List

# There are n gas stations along a circular route,
# where the amount of gas at the ith station is gas[i].
# You have a car with an unlimited gas tank and
# it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station.
# You begin the journey with an empty tank at one of the gas stations.
# Given two integer arrays gas and cost,
# return the starting gas station's index if you can travel around the circuit once in the clockwise direction,
# otherwise return -1.
# If there exists a solution, it is guaranteed to be unique.


class Solution:
    def _canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            # solving for when the car starts from the ith station
            remaining_gas = 0
            can_travel = True
            for j in range(len(gas)):
                current_index = (i + j) % len(gas)
                remaining_gas += gas[current_index]
                if cost[current_index] > remaining_gas:
                    can_travel = False
                    break
                else:
                    remaining_gas -= cost[current_index]
            if can_travel:
                return i
        return -1

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # gas = [1,2,3,4,5], cost = [3,4,5,1,2]
        # [-2, -2, -2, 3, 3]
        # [-3, 4, -3, -2, 10]
        # [1, -1, -1, 4, -1, -2]
        # gas = [5,8,2,8], cost = [6,5,6,6]
        # [-1, 3, -4, 2, 2]
        # [1, 2, -3, -1, 1]
        total = 0
        candidate = 0
        current_total = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            new_current_total = current_total + diff
            if new_current_total < 0:
                current_total = 0
                candidate = i + 1
            else:
                current_total = new_current_total
        if total >= 0:
            return candidate
        else:
            return -1
