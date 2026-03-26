"""
Lab 15: Task Scheduler — A priority queue in action

Task 3: Build a TaskScheduler class using heapq.
"""

import heapq


class TaskScheduler:
    
    def __init__(self):
        self.heap = []
        self.counter = 0 

    def add_task(self, priority, description):
        heapq.heappush(self.heap, (priority, self.counter, description))
        self.counter += 1 

    def next_task(self):
        if not self.heap:
            return None 
        
        _, _, description = heapq.heappop(self.heap)
        return description 

    def peek(self):
        if not self.heap:
            return None
    
        return self.heap[0][2]

    def __len__(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0