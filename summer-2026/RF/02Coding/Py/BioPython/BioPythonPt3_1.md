# Alignment using BLAST


## Learning Objectives
    - Run shell commands in Colab
    - Install local BLAST tools in Colab and use these tools
    - Perform remote BLAST runs
    - Run the BLAST variants - blastn, blastx, and tblastx
    - Export alignment results to files

Use the BioPythonPt3_1.ipynb notebook in Google Colab to see how the
    above tasks can be performed. Note that the code is in a number 
    of different cells and we have to run "all" the cells to see the
    results


Part 1: Installing BLAST Tools in Colab

PART 2: Creating Sample Sequences and Database to make Local BLAST runs
- Continued in next cell - cell #2
- Needed to execute shell commands to: create sequences and put them into a BLAST database
- cell #3
  - run blastx
  - run tblastx

Part 3: Send a Sequence to the BLAST server and get results
- cell 4 - submit a BLAST search
- save results locally
- Read results and pring HSPs


Task 1: Download the "contaminants" sequences
- Should give us ~18 MB of FASTA sequences.
 

Tasks: Design primers sets for gene from Paper - 
- for mRNA
- genomic DNA - CDS - cross 
- genomic DNA - a single intron only
- genomic DNA - to detect alternative splice variants

  
