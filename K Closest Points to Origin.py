# K Closest Points to Origin
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
# code

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # will use quickselect

        def swap(i, j):
            temp = points[i]
            points[i] = points[j]
            points[j] = temp
        
        def calc(p):
            return p[0] * p[0] + p[1] * p[1]

        def qs(s, e, k):
            p = points[e]
            pv = calc(p)
            j = s
            for i in range(s, e):
                if calc(points[i]) < pv:
                    if i != j : swap(i, j)
                    j = j + 1
            swap(j, e)
            if j == k - 1:
                return j
            if j < k:
                return qs(j + 1, e, k)
            if j > k:
                return qs(s, j - 1, k)

        qs(0, len(points)-1, k)    
        return points[:k]