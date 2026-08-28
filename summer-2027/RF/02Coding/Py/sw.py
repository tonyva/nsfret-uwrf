#!/usr/bin/python3

# This is a Python implementation of the Smith Waterman adynamic programming
# algorithm. I found this by doing an AI-assisted Google search. 
# It looks ok and when I used the same sequences as in the Topic 6 notes
# this program gives a similar result.
#   Run this program - no inputs needed - to see the output.
# I am not sure that this works correctly - the results "seem" ok - which is
# not the same thing as being "correct"
#
# There are many implementations in Python of Smith Waterman.
#  Here are a couple more:
#    1. https://gist.github.com/radaniba/11019717
#    2. https://github.com/Seb943/Smith_Waterman_Py/blob/master/Smith-Waterman.py
#  I cannot vouch for the correctness of any of these - you may want to check
#  them before relying on them.



def smith_waterman(seq1: str, seq2: str, match=1, mismatch=0, gap=0):
    """
        Compute a local alignment of two sequences.

        Parameters:
            seq1, seq2: Strings to align
            match:    Score added for identical characters
            mismatch: Score added for differing characters
            gap:      Penalty for inserting an alignment gap
    """

    m, n = len(seq1), len(seq2)

    # 1. Initialize scoring matrix with zeros
    matrix = [[0] * (n + 1) for _ in range(m + 1)]

    max_score = 0
    max_pos = (0, 0)

    # 2. Fill the scoring matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Calculate match/mismatch score
            if seq1[i - 1] == seq2[j - 1]:
                score_diag = matrix[i - 1][j - 1] + match
            else:
                score_diag = matrix[i - 1][j - 1] + mismatch

            score_up = matrix[i - 1][j] + gap
            score_left = matrix[i][j - 1] + gap

            # Local alignment constraint: lower bound is strictly 0
            matrix[i][j] = max(0, score_diag, score_up, score_left)

            # Track the absolute maximum score and its position
            if matrix[i][j] > max_score:
                max_score = matrix[i][j]
                max_pos = (i, j)

    # 3. Traceback phase starting from the highest score
    align1, align2 = [], []
    i, j = max_pos

    while matrix[i][j] > 0:
        current_score = matrix[i][j]

        # Check if move came from diagonal
        if seq1[i - 1] == seq2[j - 1]:
            expected_diag = current_score - match
        else:
            expected_diag = current_score - mismatch

        if i > 0 and j > 0 and matrix[i - 1][j - 1] == expected_diag:
            align1.append(seq1[i - 1])
            align2.append(seq2[j - 1])
            i -= 1
            j -= 1
        # Check if move came from up (gap in seq2)
        elif i > 0 and matrix[i - 1][j] == current_score - gap:
            align1.append(seq1[i - 1])
            align2.append('-')
            i -= 1
            # Check if move came from left (gap in seq1)
        elif j > 0 and matrix[i][j - 1] == current_score - gap:
            align1.append('-')
            align2.append(seq2[j - 1])
            j -= 1
        else:
            break

    # Reverse the alignment arrays since we traced backward
    align1 = "".join(reversed(align1))
    align2 = "".join(reversed(align2))

    return max_score, align1, align2

# Example Execution
if __name__ == "__main__":
    s1 = "GCCAT"
    s2 = "GAAT"

    score, res1, res2 = smith_waterman(s1, s2)
    print(f"Optimal Local Score: {score}")
    print(f"Sequence 1 segment: {res1}")
    print(f"Sequence 2 segment: {res2}")
