"""
Lab 15: Heap Basics — Getting comfortable with heapq

Tasks 1 and 2: Explore the heapq API and work with tuple priorities.
"""

import heapq


# ── Task 1: Heap Basics ─────────────────────────────────────────────


def push_and_pop(values):
    h = []

    for v in values:
        heapq.heappush(h, v)

    result = []
    while h:
        result.append(heapq.heappop(h))

    return result 


def heapify_and_peek(values):
    if not values:
        return None
    
    h = list(values)
    heapq.heapify(h)

    return h[0]


def top_k_smallest(values, k):
    return heapq.nsmallest(k, values)


# ── Task 2: Tuple Priorities ────────────────────────────────────────


def sort_by_priority(tasks):
    """Sort tasks by priority, maintaining FIFO order for equal priorities.

    Args:
        tasks: A list of (priority, description) tuples.

    Returns:
        A list of description strings in priority order.
        Same-priority tasks appear in their original order.
    """
    # TODO: Use a heap with a sequence counter as tiebreaker
    pass