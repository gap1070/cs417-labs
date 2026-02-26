"""
Lab 10: Searching — From Linear Scan to Divide and Conquer

In this lab you will implement two search algorithms and then
create versions that count comparisons so you can measure
their performance.

Complete the four functions marked with TODO.
Do NOT change the function signatures.

Run tests:
    pytest -v
"""


# ── TODO 1: Sequential Search ────────────────────────────────────


def sequential_search(a_list, target):
    for item in a_list:
        if item == target:
            return True 
    return False


# ── TODO 2: Binary Search ────────────────────────────────────────


def binary_search(a_list, target):
    first = 0
    last = len(a_list) - 1 

    while first <= last:
        mid = (first + last) // 2 

        if a_list[mid] == target:
            return True 
        elif target < a_list[mid]:
            last = mid - 1 
        else: 
            first = mid + 1

    return False 


# ── TODO 3: Counted Versions ─────────────────────────────────────


def sequential_search_counted(a_list, target):
    comparisons = 0 

    for item in a_list:
        comparisons += 1
        if item == target:
            return True, comparisons 
        
    return False, comparisons


def binary_search_counted(a_list, target):
    first = 0 
    last = len(a_list) - 1
    comparisons = 0 

    while first <= last:
        mid = (first + last) // 2 
        comparisons += 1 

        if a_list[mid] == target:
            return True, comparisons 
        elif target < a_list[mid]:
            last = mid - 1 
        else:
            first = mid + 1

    return False, comparisons 