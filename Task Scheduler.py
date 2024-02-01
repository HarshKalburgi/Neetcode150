# Task Scheduler
# # Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a 
# different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time,
# the CPU could complete either one task or just be idle.
# However, there is a non-negative integer n that represents the cooldown period between two same tasks 
# (the same letter in the array), that is that there must be at least n units of time between any two same tasks.
# Return the least number of units of times that the CPU will take to finish all the given tasks.

# code

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ## RC ##
        ## APPROACH : HASHMAP ##
        ## LOGIC : TAKE THE MAXIMUM FREQUENCY ELEMENT AND MAKE THOSE MANY NUMBER OF SLOTS ##
        ##  Slot size = (n+1) if n= 2 => slotsize = 3 Example: {A:5, B:1} => ABxAxxAxxAxxAxx => indices of A = 0,2 and middle there should be n elements, so slot size should be n+1
        
        ## Ex: {A:6,B:4,C:2} n = 2
        ## final o/p will be
        ## slot size / cycle size = 3
        ## Number of rows = number of A's (most freq element)
        # [
        #     [A, B,      C],
        #     [A, B,      C],
        #     [A, B,      idle],
        #     [A, B,      idle],
        #     [A, idle,   idle],
        #     [A   -        - ],
        # ]
        #
        # so from above total time intervals = (max_freq_element - 1) * (n + 1) + (all elements with max freq)
                                     # ans   =     rows_except_last   * columns +        last_row
            
            
        ## but consider {A:5, B:1, C:1, D:1, E:1, F:1, G:1, H:1, I:1, J:1, K:1, L:1} n = 1
        ## total time intervals by above formula will be 4 * 2 + 1 = 9, which is less than number of elements, which is not possible. so we have to return max(ans, number of tasks)
        
        
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(1) ##

        freq = collections.Counter(tasks)
        max_freq = max(freq.values())
        freq = list(freq.values())
        max_freq_ele_count = 0                 # total_elements_with_max_freq, last row elements
        i = 0
        while( i < len(freq)):
            if freq[i] == max_freq:
                max_freq_ele_count += 1
            i += 1
            
        ans = (max_freq - 1) * (n+1) + max_freq_ele_count
        
        return max(ans, len(tasks))