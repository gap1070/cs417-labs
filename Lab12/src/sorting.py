"""
Lab 12: Breaking the O(n^2) Barrier

In this lab you will complete the core logic for three advanced
sorting algorithms: shell sort, merge sort, and quicksort.

The recursive structure and helper scaffolding are provided —
your job is to fill in the key mechanisms:
  - Shell sort: the gap insertion sort helper (Task 1)
  - Merge sort: the merge step (Task 2)
  - Quicksort: the partition (Task 3)

Counted versions are provided complete for use in the analysis
notebook.

Complete the THREE sections marked with TODO.
Do NOT change the function signatures or the provided code.

Run tests:
    pytest -v
"""


# ── TODO 1: Shell Sort — Gap Insertion Sort ───────────────────────


def _gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap): 
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap 

        a_list[position] = current_value


def shell_sort(a_list):
    """
    Sort a_list in ascending order using Shell sort.

    DO NOT MODIFY — this function is complete.
    It calls your _gap_insertion_sort helper above.
    """
    gap = len(a_list) // 2
    while gap > 0:
        for start_position in range(gap):
            _gap_insertion_sort(a_list, start_position, gap)
        gap = gap // 2
    return a_list


# ── TODO 2: Merge Sort — The Merge Step ──────────────────────────


def merge_sort(a_list):
    if len(a_list) <= 1:
        return a_list

    mid = len(a_list) // 2
    left = a_list[:mid]
    right = a_list[mid:]

    merge_sort(left)
    merge_sort(right)

    # ── MERGE STEP: fill in below ──────────────────────────
    # Combine the sorted left and right halves back into a_list.
    # Initialize: i = 0, j = 0, k = 0
    # Then write the three while loops described above.

    i = 0 
    j = 0 
    k = 0 

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            a_list[k] = left[i]
            i += 1
        else:
            a_list[k] = right[j]
            j += 1 
        k += 1 

    while i < len(left):
        a_list[k] = left[i]
        i += 1 
        k += 1 

    while j < len(right):
        a_list[k] = right[j]
        j += 1 
        k += 1 

    return a_list


# ── TODO 3: Quicksort — The Partition ─────────────────────────────


def _partition(a_list, first, last):
    pivot_value = a_list[first]

    left_mark = first + 1
    right_mark = last
    done = False

    while not done:

        while left_mark <= right_mark and a_list[left_mark] <= pivot_value:
            left_mark += 1 

        while left_mark <= right_mark and a_list[right_mark] >= pivot_value:
            right_mark -= 1 

        if right_mark < left_mark:
            done = True
        else:
             a_list[left_mark], a_list[right_mark] = a_list[right_mark], a_list[left_mark]

    a_list[first], a_list[right_mark] = a_list[right_mark], a_list[first]

    return right_mark


def _quick_sort_helper(a_list, first, last):
    """Recursive quicksort. DO NOT MODIFY."""
    if first < last:
        split_point = _partition(a_list, first, last)
        _quick_sort_helper(a_list, first, split_point - 1)
        _quick_sort_helper(a_list, split_point + 1, last)


def quick_sort(a_list):
    """
    Sort a_list in ascending order using quicksort.

    DO NOT MODIFY — this function is complete.
    It calls _quick_sort_helper, which calls your _partition.
    """
    if len(a_list) > 1:
        _quick_sort_helper(a_list, 0, len(a_list) - 1)
    return a_list


# ── Counted Versions (PROVIDED — use in the analysis notebook) ────


def merge_sort_counted(a_list):
    """
    Merge sort that also counts comparisons and data moves.

    Returns:
        (sorted_list, comparisons, data_moves)

    You do NOT need to modify this function.
    Use it in the analysis notebook to measure performance.
    """
    counts = [0, 0]  # [comparisons, data_moves]

    def _merge_sort(lst):
        if len(lst) > 1:
            mid = len(lst) // 2
            left = lst[:mid]
            right = lst[mid:]
            _merge_sort(left)
            _merge_sort(right)
            i = j = k = 0
            while i < len(left) and j < len(right):
                counts[0] += 1
                if left[i] <= right[j]:
                    lst[k] = left[i]
                    i += 1
                else:
                    lst[k] = right[j]
                    j += 1
                counts[1] += 1
                k += 1
            while i < len(left):
                lst[k] = left[i]
                counts[1] += 1
                i += 1
                k += 1
            while j < len(right):
                lst[k] = right[j]
                counts[1] += 1
                j += 1
                k += 1

    _merge_sort(a_list)
    return (a_list, counts[0], counts[1])


def quick_sort_counted(a_list):
    """
    Quicksort that also counts comparisons and exchanges.

    Returns:
        (sorted_list, comparisons, exchanges)

    You do NOT need to modify this function.
    Use it in the analysis notebook to measure performance.
    """
    counts = [0, 0]  # [comparisons, exchanges]

    def _partition(lst, first, last):
        pivot_value = lst[first]
        left_mark = first + 1
        right_mark = last
        done = False
        while not done:
            while left_mark <= right_mark and lst[left_mark] <= pivot_value:
                counts[0] += 1
                left_mark += 1
            while left_mark <= right_mark and lst[right_mark] >= pivot_value:
                counts[0] += 1
                right_mark -= 1
            if right_mark < left_mark:
                done = True
            else:
                lst[left_mark], lst[right_mark] = lst[right_mark], lst[left_mark]
                counts[1] += 1
        lst[first], lst[right_mark] = lst[right_mark], lst[first]
        counts[1] += 1
        return right_mark

    def _qs(lst, first, last):
        if first < last:
            sp = _partition(lst, first, last)
            _qs(lst, first, sp - 1)
            _qs(lst, sp + 1, last)

    if len(a_list) > 1:
        _qs(a_list, 0, len(a_list) - 1)
    return (a_list, counts[0], counts[1])