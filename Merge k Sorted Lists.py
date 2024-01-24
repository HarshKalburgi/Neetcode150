# Merge k Sorted Lists
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

# code:

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode(None)
        curr = head
        h = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next
        
        while h:
            val, i = heapq.heappop(h)
            curr.next = ListNode(val)
            curr = curr.next
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next
        
        return head.next