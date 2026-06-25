# Coverage needed for a good genome assembly

An important problem to solve in assembling a genome is that of the number
of reads we would need to "cover" each nucleotide in the final assembly.
That is, how many times do we have to see a nucleotide at each position to
say confidently what should go in that position?

The Samantha paper does not explicitly state what coverage they need for 
the tetraploid genome. Resolving each of the four "copies" of the 7 chromosomes
will certainly require more coverage than a haploid or diploid genome.
The paper does not mention the coverage needed but taking all the sequence data
as one quantity and dividing that by the size of the final haplotype-resolved
genome, they achieve an average coverage of 500!

The mathematical foundation for genome assembly coverage relies heavily on
probability theory and information theory. At its core, the problem is modeled
as a stochastic covering problem, which establishes how many random sequenced
fragments (reads) are required to reconstruct a contiguous sequence of a
genome without leaving any gaps.

1. The Lander-Waterman Model
The fundamental framework for coverage math was established by Eric Lander and
Michael Waterman in 1988. They treated genome sequencing as a Poisson process
where short reads are dropped randomly and uniformly across a haploid genome.
Ref:
Lander ES, Waterman MS. Genomic mapping by fingerprinting random clones:
a mathematical analysis. Genomics. 1988 Apr 1; 2(3):231–9. 
(http://dx.doi.org/10.1016/0888-7543(88)90007-9)

To assemble a genome of length "n" base pairs  using Nr reads, each of average
length, m, the average depth of coverage, C is:
C = (m Nr)/n

Assuming the reads are random samples, the number of reads covering a specific
nucleotide in the genome will have a Poisson distribution.
--> the probability that a nucleotide will be covered k times will be:
P(X=k) = e^(-C) C^k / k!

This implies that the probability that a specific nucleotide will not be in any
read will be P(X=0) which will be e^(-C). This will also be the expected
fraction of the genome that will have 0 coverage: e^(-C) and the proportion of 
the genome covered by at least one read will be 1 - e^(-C).

The Lander-Waterman equation for the number of reads needed to cover the
entire genome with a specific probability will be:
Nr = n ln( n/e )/m
where e is the acceptable probability of an unsequenced part 

The result is that for a genome of size "n" bases, the "total" number of 
bases in the reads should be O(n log n).




2. By combining sequencing and assembly, Nasht-ali et al. showed in 2016, that 
O( n ) may be sufficient.
Ref: 
Breaking Lander-Waterman’s Coverage Bound (2016) PLoS One 11(11): e0164888 (https://doi.org/10.1371/journal.pone.0164888)



3. There are some complicating factors in real genomes:
    1. Genomes contain repetitive sequences. 
   If the length of a repeating sequence, Rep, is greater than the read length,
   m, reads cannot be uniquely ordered without spanning the repeat.
   Resolving this will require one of two approaches:
   - paired-end sequencing
   - long-read sequencing

    2. Since C is an average, 50% of the genome will have less than half-coverage.
   i.e. there is no non-zero floor for coverage.

    3. Sequencing errors will require higher coverage.
   If the probability of sequencing error is "s", the number of
   additional reads may be proportional to 1/s ???

    4. The two main methods for genome assembly are:
    - overlap  graph
    - de Bruijn graph
   The de Bruijn method needs higher coverage to build an assembly.

    5. After years of trial and error in many genome assembly projects, 
   we have a few empirical standards for required coverage:
   Short reads (e.g. Illumina): Coverage for
      - a De Novo assembly:
          -  50x to 100x for plants/animals
          - 100x to 200x for bacterial genomes
      - reference-guided resequencing for reliable SNP detection:
          - 30x to 50x if a good reference genome is available.
   Long reads (e.g. PacBio, Ox Nano) requires 30x to 50x since these techniques
   make it easier to cover long repetitive sequences.
     - 20x to 30x for an overall standard draft of the genome structure
     - 50x to 100x for high sequence accuracy, telomere to telomere coverage, 
          separate maternal/paternal chromosomes
   Hybrid - combining Short and Long is the current gold standard
     - 20 to 30x for long reads to build thge scaffold and untangle complex repeats.
     - 30 to 50x for short reads to "polish" the final assembly
Ref: [Sequencing 101](https://www.pacb.com/blog/sequencing-101-sequencing-coverage/)

Diploid genome assembly:
Mahajan D, Jain C, Kashyap N. On the Coverage Required for Diploid Genome Assembly. IEEE Trans Comput Biol Bioinform. 2025 Nov-Dec;22(6):2491-2502. doi: 10.1109/TCBBIO.2025.3594365. PMID: 40811168.
also available at: [https://arxiv.org/pdf/2405.05734v3]


Darian JC, Kundu R, Rajaby R, Sung WK. Constructing telomere-to-telomere diploid genome by polishing haploid nanopore-based assembly. Nat Methods. 2024 Apr;21(4):574-583. doi: 10.1038/s41592-023-02141-1. Epub 2024 Mar 8. PMID: 38459383.
- [https://www.nature.com/articles/s41592-023-02141-1]








