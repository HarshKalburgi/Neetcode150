# Minimum Interval to Include Each Query
# You are given a 2D integer array intervals, where intervals[i] = [lefti, righti] describes the ith interval starting at lefti and ending at righti (inclusive). The size of an interval is defined as the number of integers it contains, or more formally righti - lefti + 1.
# You are also given an integer array queries. The answer to the jth query is the size of the smallest interval i such that lefti <= queries[j] <= righti. If no such interval exists, the answer is -1.
# Return an array containing the answers to the queries.
# code
class Solution:
	def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
		hashMap = {}
		intervals.sort()

		minHeap = []

		i_l = len(intervals)
		i = 0
		for q in sorted(queries):
			while i < i_l and intervals[i][0] <= q:
				start, end = intervals[i]
				heapq.heappush(minHeap, [(end-start+1), end])
				i += 1

			while minHeap and minHeap[0][1] < q:
				heapq.heappop(minHeap)

			hashMap[q] = minHeap[0][0] if minHeap else -1

		return [hashMap[q] for q in queries]