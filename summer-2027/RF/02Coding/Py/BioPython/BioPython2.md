# Lab 2: Reading and Writing Sequence Files

## Learning Objectives
    - Read sequences from FASTA files
    - Read sequences from GenBank files
    - Write sequences to various formats
    - Handle multiple sequences in files
    - Parse file metadata

BioPython2.ipynb should run as a Jupyter notebook. 
So far it has been tested in:  
- Google Colab

The seven parts of this notebook show you:
 1. How to create sample FASTA and GenBank files
 2. Three methods to read FASTA files:
    Parse all at once (good for small files)
    Iterate (memory efficient for large files)
    Index by ID (for random access)
 3. How to read GenBank files with annotations and features
 4. Write sequences to different formats
 5. Convert between formats (FASTA ↔ GenBank)
 6. Filters sequences and adds annotations
 7. Overview of supported formats

