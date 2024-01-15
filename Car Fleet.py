# Car Fleet
# There are n cars going to the same destination along a one-lane road. The destination is target miles away.

# You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

# A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).

# A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.
# code

class Solution:
    def carFleet(self, target: int, position, speed):
        cars_right_to_left = sorted(zip(position, speed), reverse=True)

        bottleneck = float('-inf')
        fleets = 0

        for d, s in cars_right_to_left:
            remaining_dist = target - d
            time_to_reach_target = (remaining_dist / s)

            if time_to_reach_target > bottleneck:
                bottleneck = time_to_reach_target
                fleets += 1

        return fleets