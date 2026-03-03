"""
Lab 11: Sorting — Why Big-O Isn't the Whole Story

In this lab you will implement two sorting algorithms (bubble sort
and insertion sort), an optimized variant (short bubble sort), and
counted versions that track comparisons and data moves.

Complete the five functions marked with TODO.
Do NOT change the function signatures.

Run tests:
    pytest -v
"""


# ── TODO 1: Bubble Sort ─────────────────────────────────────────


def bubble_sort(a_list):
    n = len(a_list)

    for i in range(n-1):
        for j in range(n-1-i):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]

    return a_list


# ── TODO 2: Short Bubble Sort ───────────────────────────────────


def short_bubble_sort(a_list):
    n = len(a_list)

    for i in range(n -1):
        swapped = False 

        for j in range(n - 1 - i):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
                swapped = True

        if not swapped:
            break

    return a_list


# ── TODO 3: Insertion Sort ──────────────────────────────────────


def insertion_sort(a_list):
    for i in range(1, len(a_list)):
        current_value = a_list[i]
        position = i - 1

        while position >= 0 and a_list[position] > current_value:
            a_list[position + 1] = a_list[position]
            position -= 1 

        a_list[position + 1] = current_value
    
    return a_list


# ── TODO 4: Counted Versions ────────────────────────────────────


def bubble_sort_counted(a_list):
    n = len(a_list)
    comparisons = 0 
    exchanges = 0 

    for i in range(n - 1):
        for j in range(n - 1- i):
            comparisons += 1
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
                exchanges += 1 

    return a_list, comparisons, exchanges


def insertion_sort_counted(a_list):
    comparisons = 0 
    data_moves = 0 

    for i in range(1, len(a_list)):
        current_value = a_list[i]
        position = i - 1

        while position >= 0:
            comparisons += 1
            if a_list[position] > current_value:
                a_list[position + 1] = a_list[position]
                data_moves += 1
                position -= 1
            else:
                break

        a_list[position + 1] = current_value
        data_moves += 1 

    return a_list, comparisons, data_moves