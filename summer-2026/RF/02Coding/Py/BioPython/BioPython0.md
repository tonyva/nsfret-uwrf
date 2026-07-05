# BioPython

BioPython is a library of bioinformatics code that we can use in our own
Python code. By using BioPython, we can accomplish tasks like:
- Reading or writing FASTA, GenBank, BLAST, ClustalW, and PDB data files.
- Treating DNA, RNA, and protein sequences like Python strings but with
   biological logic like automated transcription, translation, and
   computing reverse-complements.
- Interfacing with Databases online biological repositories like NCBI (Entrez),
   ExPASy, and SCOP to fetch records for use in our code.
- Analyze 3D molecular structures from molecular structure data so we can
   view specific atoms, amino acids, or chains.


# Bio

If we add "import Bio" in our Python program, when we run this program, the 
Python interpreter will try to find the Bio package  on the computer on which
we are running the program.
If it does not find it, it will say something like:
 the "module was not found" - even if it is possible that we may have put 
 the package in the wrong place.

If the Bio package is found, the Python interpreter will initialize an
area of the runtime memory used for BioPython and set up an "environment" for
BioPython code in our Python program to execute.

Some of the parts of BioPython are:
- Bio.Seq - core sequence objects and biological string logic.
- Bio.SeqIO - code for reading and writing sequence file formats.
- Bio.Entrez - used to access NCBI databases (PubMed, GenBank).
- Bio.PDB - read and manipulate 3D structural data for proteins and
   nucleic acids.
- Bio.Align - tools for creating, reading, and evaluating sequence alignments.



# Bio.Seq

This is an important Python class that we will use to set up Python objects 
that can contain DNA, RNA, or protein sequence data.

Here is some simple Python code to create a sequence of nucleotides:
```python
    from Bio.Seq import Seq\

    # Directly creates a sequence object without typing "Bio.Seq.Seq()"\
coding_dna = Seq("AGTACACTG")
    print(coding_dna)
```

The above code will make the "Seq" Python class available to our Python program
- we can create a Seq object and initialize it with a sequence of nucleotides.

Even though it may look like a regular "string", the Bio.Seq class was set up
with a lot of logic that has to do with biological sequences.

We can then do things like:
    messenger_rna = coding_dna.transcribe()\
    print(messenger_rna)                     # Output: AUGGCCAUU\

    \# Reverse the process back to DNA
    print(messenger_rna.back_transcribe())

I.e. we can "print" the sequence information. We can also transcribe or 
reverse transcribe sequences. Or even translate RNA to protein:

    protein = messenger_rna.translate()\
    print(protein)                           # Output: MAI (Methionine-Alanine)\


See [BioPython1.ipynb](BioPython1.ipynb) for example Python code that uses Seq.

# Bio.SeqRecord

A SeqRecord contains a Seq object and metadata like an accession name or number, a description, a name, etc.


# Bio.SeqIO

This is a collection of functions used for reading files using SeqIO.parse and 
SeqIO.read or writing using SeqIO.write.

We can also convert sequence data from one format to another using SeqIO.convert.

See [BioPython2.ipynb](BioPython2.ipynb) for example Python code that uses SeqIO. 

# Bio.SeqUtils

SeqUtils is a module with a lot of utility finctions to compute
mathematical or biochemical properties or do some simple pattern matching.



See [BioPython3.ipynb](BioPython3.ipynb) for example code that uses Bio.SeqUtils.

# Bio.pairwise2, Bio.Align

The pairwise2 module is an older version of code to align two sequences. 
The newer/better way of aligning things is the Bio.Align module which has
a Bio.Align.PairwiseAligner class.

See [BioPythonPt2_1.ipynb](BioPythonPt2_1.ipynb),
    [BioPythonPt2_2.ipynb](BioPythonPt2_2.ipynb), or
    [BioPythonPt2_3.ipynb](BioPythonPt2_3.ipynb)
 to see these modules in use.

# Bio.Blast

This module can handle most types of Basic Local Alignment Search Tool (BLAST)
tasks that can be done using the web interface for BLAST.

See [BioPythonPt3_1.ipynb](BioPythonPt3_1.ipynb) for examples using Bio.Blast.



