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


Task 3: Design primers sets for a particular gene
- Video on [PCR](https://www.youtube.com/watch?v=c07_5BfIDTw) explains how primers are used in PCR
- [Primer-BLAST](https://www.ncbi.nlm.nih.gov/tools/primer-blast/) is a specialized BLAST site for designing primers
- This general video [Primer Design](https://www.youtube.com/watch?v=_tXULsx1S_U) shows some considerations in designing primers
- Video showing how to use the [Integrated Genome Browser](https://www.youtube.com/watch?v=x_lsZEgfwuI) to design primers for Arabidopsis

Task 4: human KCNH2 gene
- Start at the [NCBI Genome Data Viewer](https://www.ncbi.nlm.nih.gov/gdv/)
- Search in genome for KCNH2
- We will be "placed in" Chromosome 7
- Choose KCNH2 in the "Graphical view" and choose Gene ID 3757
- Scroll down to "Genomic regions ...", notice that the coding strand is the reverse complement
- Choose the FASTA view and notice that this is a long genomic sequence
- Go back and go to the GenBank view - we can see the places where the mRNA overlaps with the genomic DNA
- Go back and right-click the KCHN2 sequence again and choose CCDS5910.1
- Scroll down to the bottom of the Consensus CDS protein set page to see the nucleotides sequence of exons.
- The protein sequence is listed below it and we can see the correspondence with the nucleotides
- In some places we can see where a codon is split (shown as a red amino acid letter) between exons.
- Go "back" to te tab where the Genomic Regions is shown, right-click the CDS and choose "Primer BLAST"
- In primer BLAST, note that you can choose
    - where we want the Forward Primer to start
    - where the Reverse Primer should end
    - what exactly we want for Exon and Intron junctions, whether we want to include Introns
    - a LOT of Advanced parameters that have to do with biochemical properties!
- Click "Get Primers" - check your results and explain what they mean.

Task 5: Rosa Rugosa Flowering genes
The [Rosa rugosa genome](https://www.ncbi.nlm.nih.gov/assembly/GCF_958449725.1/) has 
an [MFT gene](https://www.ncbi.nlm.nih.gov/nuccore/XM_062169648.1) 
situated in [R. rugosa genome at](https://www.ncbi.nlm.nih.gov/nuccore/NC_084823.1?from=56930519&to=56932052&report=genbank&strand=true)
on Chromosome 4 (https://www.ncbi.nlm.nih.gov/nuccore/NC_084823.1)- 

With this information, explain the steps we should follow to design PCR primers so that we can obtain:
1. the 5'-UTR and first intron
2. the complete genomic region
3. the first exon, first intron, and second exon
4. all the exons without any of the introns
5. the last exon and the 3'-UTR
How big will each of these PCR "products" be?



- for [mRNA](https://www.ncbi.nlm.nih.gov/nuccore/KY928070.1) or HQ174211.1
- [Genomic sequence](https://www.ncbi.nlm.nih.gov/nuccore/HE863824.1)
- (https://www.ncbi.nlm.nih.gov/nuccore/HQ174211.1?report=graph)
- genomic DNA - CDS - cross exon/intron boundary
- genomic DNA - a single intron only
- genomic DNA - to detect alternative splice variants

Also see:\
- The [Genome portal for R. chinensis](https://lipm-browsers.toulouse.inra.fr/pub/RchiOBHm-V2/)
- The [NCBI Genome Viewer](https://www.ncbi.nlm.nih.gov/gdv/browser/genome/?id=GCF_002994745.2)
- Browsing the R. chinensis genome in [rosacea.org](https://www.rosaceae.org/jbrowse/index.html?data=data%2Frosa%2Frchinensis_v1.0&loc=Chr01%3A28776081..30926287&tracks=DNA%2Cv1.0_genes%2Cv1.0_transcripts%2CQTL_Sept24&highlight=)
- A [2024 post](https://forum.rosehybridizers.org/t/questions-about-roksn-and-roksn-genotyping/12437https://forum.rosehybridizers.org/t/questions-about-roksn-and-roksn-genotyping/12437) in the Rose Hybridizers Association forum.
- [Wikipedia article](https://en.wikipedia.org/wiki/Flowering_plant)
