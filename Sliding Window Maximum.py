# Sliding Window Maximum
# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window.
#  Each time the sliding window moves right by one position.

# Return the max sliding window.
# code
from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        result = []
        window = deque()

        for i in range(len(nums)):
            # remove indices that are out of the current window
            while window and window[0] < i - k + 1:
                window.popleft()
            
            # remove indices of elements smaller than the num
            while window and nums[window[-1]] < nums[i]:
                window.pop()
            
            # append the current index to the window
            window.append(i)

            # add the maximum element to the result
            if i >= k - 1:
                result.append(nums[window[0]])

        return result
