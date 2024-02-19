# Gas Station
# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique
# code

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        tank = idx = 0
        for i in range(len(gas)):
            tank+= gas[i]-cost[i] 
            if tank < 0: tank, idx = 0, i+1
        return idx 

        print(f"cost: {cost}")
        print(f"gas: {gas}")
        tank = 0
        for i in range(len(cost)):
            # find where we can start
            if cost[i] > gas[i]+tank:
                continue
            start = i    
            tank += gas[i]
            print("tank", tank)
            for j in range(start+1, len(cost)):
                if cost[i] > gas[i]:
                    print("inside", j)
        return -1