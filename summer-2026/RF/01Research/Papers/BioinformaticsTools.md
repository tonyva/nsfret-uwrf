# Bioinformatics programs used in the Samantha paper

Besides standard tools like Blast, a number of specialized programs were
used to set up the tetraploid genome.

## De novo genome assembly

1. hifiasm for assembly using long reads. Cheng et al. 2021 Nature Methods
   C++ code in GitHub

2. Contaminating sequences were found using regular blastn

3. Cooler python library. Available as a docker image from BioContainer

4. minimap2 by Li (2018) is used for many tasks

5. The HiPore-C pipeline uses many programs. There is a GitHub site for this.

6. LACHESIS - chromosome-scale scaffolding. Burton (2013)

7. HiCUP was used to anchor contigs to chromosomes. There is a 2015 F1000 paper
   that has good diagrams.

8. nPhase to combine long and short reads. Abou Saada (2021) 
   Python code is available at GitHub

9. SyR1 Synteny and Rearrangement Identifier code for Synteny analysis
   to find genomic rearrangements (such as homoeologous exchanges),
   translocations, and local sequence differences by comparing the
   whole-genome assemblies of different haplotypes and related species.
   2019 paper; code is on Zenodo
  

## Quality control and evaluation of genome assembly

1. ALLMAPS

2. BUSCO

3. LAI

4. KAT

5. Merqury


## RNA-Seq and Transcriptome Assembly

1. Trimmomatic - standard tool for trimming, quality control, and filtering of raw Illumina RNA-Seq sequencing reads.

2. Trinity for de novo assembly of full-length transcriptomes from RNA-Seq data.


## Transposable Element and Repeat Annotation

1. RepeatModeler2  for automated, de novo genomic discovery and modeling of
   transposable element families.

2. RepeatMasker to screen and mask repetitive elements and low-complexity DNA
   sequences across the newly assembled genome using established databases 
   like Repbase and Dfam.

3. LTRharvest for de novo detection of Long Terminal Repeat retrotransposons.

4. MITE-Hunter for finding miniature inverted-repeat transposable elements
   (MITEs) in genomic sequences.


## Gene Prediction & Structural Annotation

1. PASA (Program to Assemble Spliced Alignments) to incorporate RNA-Seq transcript alignments into gene structure annotations to identify splicing variations.

2. AUGUSTUS for ab initio eukaryotic gene prediction based on genomic, EST, and protein alignment profiles.

3. SNAP hidden Markov model-based gene finder used for identifying genes in the novel rose genome.

4. GlimmerHMM / TigrScan ab initio HMM gene finders trained to identify exon-intron boundaries and coding sequences.

5. EVidenceModeler (EVM) to combine the ab initio gene predictions
    (from AUGUSTUS, SNAP, etc.), transcript alignments, and protein homologies
    into a single, highly reliable consensus automated eukaryotic gene
    structure annotation.

## Functional Annotation Databases 

These are not standalone algorithms
- the annotation pipelines rely computationally
on aligning against database sequences.

1. BLAST queries against the GenBank nt/nr databases.

2. InterProScan mappings against the InterPro database for protein domain and motif identification.

3. UniProt (Swiss-Prot/TrEMBL) for comparative protein annotation.


