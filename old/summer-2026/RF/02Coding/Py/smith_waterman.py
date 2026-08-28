def smith_waterman(seq1, seq2, match=2, mismatch=-1, gap=-1):
    """
    Implements the Smith-Waterman algorithm for local sequence alignment.
    """
    m, n = len(seq1), len(seq2)
    # Initialize the scoring matrix with zeros
    score_matrix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    max_score = 0
    max_pos = (0, 0)

    # Fill the scoring matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Calculate score for match/mismatch
            if seq1[i-1] == seq2[j-1]:
                diag = score_matrix[i-1][j-1] + match
            else:
                diag = score_matrix[i-1][j-1] + mismatch
            
            # Calculate scores for gaps
            up = score_matrix[i-1][j] + gap
            left = score_matrix[i][j-1] + gap
            
            # Smith-Waterman: score is at least 0
            score_matrix[i][j] = max(0, diag, up, left)
            
            # Track the maximum score for the traceback starting point
            if score_matrix[i][j] >= max_score:
                max_score = score_matrix[i][j]
                max_pos = (i, j)

    # Traceback
    align1, align2 = "", ""
    i, j = max_pos
    
    while i > 0 and j > 0 and score_matrix[i][j] > 0:
        current_score = score_matrix[i][j]
        diagonal_score = score_matrix[i-1][j-1]
        up_score = score_matrix[i-1][j]
        left_score = score_matrix[i][j-1]
        
        if seq1[i-1] == seq2[j-1]:
            s = match
        else:
            s = mismatch
            
        if current_score == diagonal_score + s:
            align1 += seq1[i-1]
            align2 += seq2[j-1]
            i -= 1
            j -= 1
        elif current_score == up_score + gap:
            align1 += seq1[i-1]
            align2 += "-"
            i -= 1
        else:
            align1 += "-"
            align2 += seq2[j-1]
            j -= 1

    return align1[::-1], align2[::-1], max_score

if __name__ == "__main__":
    # Example usage:
    s1 = "TGTTACGG"
    s2 = "GGTTGA"
    a1, a2, score = smith_waterman(s1, s2)

    print(f"Sequence 1: {s1}")
    print(f"Sequence 2: {s2}")
    print(f"--- Local Alignment ---")
    print(f"Aligned 1: {a1}")
    print(f"Aligned 2: {a2}")
    print(f"Optimal Local Alignment Score: {score}")
