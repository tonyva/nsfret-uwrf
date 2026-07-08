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

Task 2: Print BLAST results in sorted order using DataFrame:
-  ```python
   for hsp in alignment.hsps:
       data.append({ "Accession": alignment.accession, ... ```
-  ```python df = pd.DataFrame(data)
   # Sort by best E-value
   df = df.sort_values("E-Value")```
- Save dataframe data as a .CSV file:
  ```pythondf.to_csv("blast_summary.csv", index=False)```


Task 3: Design primers sets for the RoKSN gene
- for [mRNA](https://www.ncbi.nlm.nih.gov/nuccore/KY928070.1)
- [Genomic sequence](https://www.ncbi.nlm.nih.gov/nuccore/HE863824.1)
- genomic DNA - CDS - cross exon/intron boundary
- genomic DNA - a single intron only
- genomic DNA - to detect alternative splice variants

Also see:\
- Browsing the R. chinensis genome in [rosacea.org](https://www.rosaceae.org/jbrowse/index.html?data=data%2Frosa%2Frchinensis_v1.0&loc=Chr01%3A28776081..30926287&tracks=DNA%2Cv1.0_genes%2Cv1.0_transcripts%2CQTL_Sept24&highlight=)
- A [2024 post](https://forum.rosehybridizers.org/t/questions-about-roksn-and-roksn-genotyping/12437https://forum.rosehybridizers.org/t/questions-about-roksn-and-roksn-genotyping/12437) in the Rose Hybridizers Association forum.
- [Wikipedia article](https://en.wikipedia.org/wiki/Flowering_plant)
