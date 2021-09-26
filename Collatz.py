#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C)
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------


def collatz_read(s):
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------


def collatz_eval(i, j):
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """

    # implemented simple solution so far
    max_cycle = 1
    current_cycle = 1

    if i > j:
        holder = j
        j = i
        i = holder
    
    index = i
    
    if ((i < 1) or (i > 999999)):
        return 0
    if ((j < 1) or (j > 999999)):
        return 0
    if isinstance(i, int) and isinstance(j, int):
        while i <= j:
            while index != 1:
                if index%2 == 0:
                    index /= 2
                else:
                    index = 3*index + 1

                current_cycle += 1

            if (max_cycle < current_cycle):
                max_cycle = current_cycle

            current_cycle = 1
            i += 1
            index = i
            
    # <your code>
    return max_cycle

# -------------
# collatz_print
# -------------


def collatz_print(w, i, j, v):
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------


def collatz_solve(r, w):
    """
    r a reader
    w a writer
    """
    for s in r:
        i, j = collatz_read(s)
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
