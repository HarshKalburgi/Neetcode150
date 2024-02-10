# Cheapest Flights Within K Stops
# There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

# You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.
# code


import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        grid=[[] for i in range(n)]
        for frm,to,cst in flights:
            grid[frm].append((cst,to))
        
        st=[(0,0,src)]
        heapq.heapify(st)
        css=[(float("infinity"),float("infinity"))]*n
        css[src]=(0,0)
        while st:
            cst,stop,x=heapq.heappop(st)
            if x==dst:
                return cst
            if stop<=k:
                for ct,to in grid[x]:
                    if css[to][0]>ct+cst or css[to][1]>stop+1:
                        css[to]=(ct+cst,stop+1)
                        heapq.heappush(st,(cst+ct,stop+1,to))

        return -1


        