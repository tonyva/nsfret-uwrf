# Biopython's Alignment Module (Modern Approach)


## Learning Objectives
    - Use the modern Bio.Align module
    - Perform alignments with BLOSUM matrices
    - Visualize alignments
    - Work with alignment objects

Use the BioPythonPt2_2.ipynb notebook in Google Colab to see how the above tasks can be performed.

Part 1: 
Compared to the BioPythonPt2_2.ipynb notebook, this one uses the Align package in BioPython. This is the "new" way to do sequence alignment - more "object oriented"

Part 2: This part uses the same 2 sequences as in the BioPythonPt2_2.ipynb notebook's Part 2. Note: only the last two nucleotides are different.
- This time we use "Align" rather than "pairwise2"

Part 3: Display the details of sequence comparison

Part 4: Global vs. Local alignment -- notice the big difference in the two alignments

Part 5: Protein alignments
- BLOSUM and PAM matrices -- see Topic 6 slides 48,49 and 73-79
Part 6: 
-  this notebook uses Pandas.DataFrame to print BLOSUM and PAM matrices in Part 6
-  

Part 7: "Draw" alignment
- Task: change the format_alignment function code to print a "x" for each mismatch

Part 8: Batch alignment - 3 sequences using one scoring matrix - 1 reference and 2 to compare
- Another use of Pandas.DataFrame to pring an array of sequence comparisons
- Task: add a 4th sequence - does the code do an additional batch alignment?

- Task: Aligning "primers": set up 4 20-nt "primer" sequences that are exact matches of 4 parts of Seq1 (the reference sequence)
- Run and check "goodness" - are there better scoring matrices that can give us better alignments?





