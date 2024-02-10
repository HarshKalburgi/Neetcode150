# Reconstruct Itinerary
# You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

# All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj={}
        for ticket in tickets:
            adj[ticket[0]]=[]
            adj[ticket[1]]=[]

        for ticket in tickets:
            adj[ticket[0]].append(ticket[1])

        for l in adj.values():
            l.sort()

        ans=[]
        def helper(node):
            while adj[node]:
                helper(adj[node].pop(0))

            ans.append(node)
        helper("JFK")
        return reversed(ans)                   
        