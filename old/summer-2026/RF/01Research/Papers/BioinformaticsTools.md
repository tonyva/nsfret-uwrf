# Bioinformatics programs used in the 2024 Samantha paper

Besides standard tools like Blast, a number of specialized programs were
used to set up the tetraploid genome.

## De novo genome assembly

1. hifiasm for assembly using long reads. Cheng et al. 2021 Nature Methods
   C++ code in GitHub

2. Contaminating sequences were found using regular blastn

3. Cooler python library. Available as a docker image from BioContainer

4. Minimap2 by Li (2018) is the standard tool for mapping PacBio HiFi long reads to reference genomes.

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
   2019 paper; Python code is on Zenodo
  

## Quality control and evaluation of genome assembly

1. ALLMAPS is part of a Python toolkit developed by Haibao Tang at the Venter Institute. The jcvi suite of programs rely on BioPython to handle data formats, genomic sequences, and for scaffolds. 

2. BUSCO explicitly requires Biopython as a core dependency - uses Biopython's SeqIO and SearchIO modules to parse input FASTA files, handle genome/transcriptome sequences, and process the outputs of the HMMER and BLAST/protein alignments it runs in the background.

3. LAI

4. KAT

5. Merqury - written in C/C++ 


## RNA-Seq and Transcriptome Assembly

1. Trimmomatic - standard tool for trimming, quality control, and filtering of raw Illumina RNA-Seq sequencing reads. It uses Java.

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

2. AUGUSTUS for ab initio eukaryotic gene prediction based on genomic, EST, and protein alignment profiles  - written in C/C++

3. SNAP hidden Markov model-based gene finder used for identifying genes in the novel rose genome.

4. GlimmerHMM / TigrScan ab initio HMM gene finders trained to identify exon-intron boundaries and coding sequences  - written in C/C++

5. EVidenceModeler (EVM) to combine the ab initio gene predictions
    (from AUGUSTUS, SNAP, etc.), transcript alignments, and protein homologies
    into a single, highly reliable consensus automated eukaryotic gene
    structure annotation.

## Functional Annotation Databases 

These are not standalone algorithms
- the annotation pipelines rely computationally
on aligning against database sequences.

1. BLAST queries against the GenBank nt/nr databases.

2. InterProScan mappings against the InterPro database for protein domain and motif identification; uses Java.

3. UniProt (Swiss-Prot/TrEMBL) for comparative protein annotation.

# Bioinformatics programs used in the 2026 Pangenome paper

Besides some of the above tools, many other programs were used to do the Pangenome analysis.\

## Pangenome Graph Construction & Comparative Genomics

1.    PGGB (Pangenome Graph Builder) / vg: Used for building, analyzing, and visualizing pangenome graphs to capture widespread structural variations (SVs) across the different Rosa accessions.

2.    Sourmash: Used for large-scale, k-mer-based sequence comparisons to quickly estimate sequence similarities and divergence across the numerous genomes.

## Phylogenomics & Evolutionary Modeling

1.    OrthoFinder for high-accuracy clustering of single-copy orthologous gene groups across the various Rosa species and outgroups. Used to cluster genes and identify single-copy orthologous gene groups. The core algorithm uses external binaries - BLAST, Diamond, MCL - it uses BioPython to parse sequences, manipulate phylogenetic trees and handle sequence records.

2.    MAFFT for rapid multiple sequence alignment of the orthologous genes.

3.    IQ-TREE 2 for efficient maximum-likelihood phylogenetic tree inference based on the genomic data.

4.    MCMCTree (from the PAML package) to estimate species divergence times with time calibrations based on fossil/database records.

5.    CAFE5 to model and analyze the evolutionary contraction and expansion of gene families across the phylogenetic tree.

6.    Dsuite to calculate ABBA-BABA statistics (D-statistics) to formally test for ancient hybridization, gene flow, and introgression among different sections of the Rosa subgenus.

7.    PSMC (Pairwise Sequentially Markovian Coalescent) to infer the historical effective population size and demographic history of the species.

## Long-Read Mapping & Deep Learning Variant Calling

(The 2024 paper relied heavily on short-read mapping tools; the 2026 paper adapted to HiFi long reads and modern AI callers)


1.    Samblaster for fast marking of read duplicates and extracting structural variant reads.

2.    DeepVariant deep neural network-based tool developed by Google used for highly accurate SNP and small-indel variant calling, substituting traditional callers like GATK.

3.    GLnexus for scalable joint genotyping and the merging of genomic VCFs (gVCFs) generated by DeepVariant.

## Polyploid Phasing, Subgenome Profiling, and Hi-C Analysis

1.    Smudgeplot & GenomeScope 2.0 
      - Reference-free, k-mer-based profiling tools used to estimate ploidy levels, heterozygosity, and subgenome structural proportions (especially for complex hybrids like the tetraploid R. gallica).

2.    Juicer to process Hi-C data into loop-resolution contact maps for scaffold validation.

3.    Bionano RefAligner to align optical consensus maps (cmaps) to phase assemblies and validate structural haplotypes.

4.    calc_switcherr & polyswitch - Custom pipelines designed specifically to estimate and validate switch error rates for highly accurate haplotype phasing.

5.    ALLHiC for allele-aware, chromosome-scale assembly and scaffolding of autopolyploid genomes based on Hi-C data.

## Transcriptomics & Automated Annotation

1.    EDTA (Extensive de-novo TE Annotator) replaced the piecemeal TE tools of 2024 (like LTRharvest and RepeatModeler) with a single, highly streamlined machine-learning pipeline for benchmarking transposable elements.

2.    HiSAT2 for fast, spliced alignment of RNA-seq data to the genomes.

3.    StringTie & Ballgown were used along with HiSAT2 for transcript-level assembly, expression analysis, and read quantification.


