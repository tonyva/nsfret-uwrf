The following questions will help you understand why reserchers use the Basic Local Alignment Search Tool[BLAST](https://en.wikipedia.org/wiki/BLAST_(biotechnology))

There are a number of databases we can search and a number of BLAST program variants we can use. Let's take a look at the main ones:

1. blastn - this is usually used to search in a database of neucleotide sequences for a (query) sequence that we may know a lot about or a sequence we do not know much about apart from the sequence itself.
   Use this input sequence which is actually one that we know much about but for this exercise, we are curious to see what similar sequences we can find:\
\>NC_003888 \
ATGCCACCCATGCTGTCCGGTCTTCTGGCCAGATTGGTCAAACTGCTGCTCGGGCGCCACGGCAGTGCGC\
TGCACTGGAGGGCCGCGGGTGCCGCGACGGTCCTCCTGGTGATCGTCCTCCTCGCGGGCTCGTACTTGGC\
CGTCCTGGCTGAGCGCGGCGCACCGGGCGCGCAGCTGATCACGTATCCGCGGGCGCTGTGGTGGTCCGTG\
GAGACCGCGACGACCGTCGGCTACGGCGACCTGTACCCCGTGACTCTGTGGGGCCGGCTCGTGGCCGTGG\
TGGTGATGGTCGCCGGGATCACCTCCTTCGGTCTGGTGACCGCCGCGCTGGCCACCTGGTTCGTCGGCCG\
GGAACAAGAGCGCCGGGGCCACTTCGTGCGCCACTCCGAGAAGGCCGCCGAGGAGGCGTACACGCGGACG\
ACCCGGGCGCTGCACGAGCGTTTCGACCGTTTGGAGCGAATGCTCGACGACAACCGCCGGTGA

What other "homologous" sequences exist in the database? Can we say whether this sequence might have a coding region? Does it code for a complete gene? Or does it just code for a part of a gene?



2. blastp - usually used to search in a database of protein sequences for a protein query sequence - that we may know a lot about or one that we do not know much about.
   Use this protein sequence as the query:\
\>WP_003971485\
MPPMLSGLLARLVKLLLGRHGSALHWRAAGAATVLLVIVLLAGSYLAVLAERGAPGAQLITYPRALWWSV\
ETATTVGYGDLYPVTLWGRLVAVVVMVAGITSFGLVTAALATWFVGREQERRGHFVRHSEKAAEEAYTRT\
TRALHERFDRLERMLDDNRR

Based on the BLASTP results, what can we say about what parts of the query amino acid sequence was conserved in other species? Is it likely to be a complete protein sequence?


3. blastx - to search in a protein sequence database with a nucleotide query sequence
   Use this nucleotide sequence - assume that it was recently sequenced and that we do not know much about it:\
\>NM_001251647\
TACATTATGTATGCATTTGGCGTAAGTATATGAGAGAGTGAGTACTACTACTGCGAAGCAAAACCAGAGA\
GACATGAGAAGCTGTGTGTGTTACACGCTTTTATTGTTTGTTTTCTTCATATGGCTACACGTGGCAACGT\
GTTCTTCGTTCAGTGACATGGATGCGCTGCTGAAGCTGAAGGAGTCCATGAAGGGAGACAGAGCCAAAGA\
CGACGCGCTCCATGACTGGAAGTTTTCCACGTCGCTTTCTGCACACTGTTTCTTTTCAGGTGTATCTTGC\
GACCAAGAACTTCGAGTTGTTGCTATCAACGTCTCCTTTGTTCCTCTCTTCGGCCACGTTCCGCCGGAGA\
TCGGAGAATTGGACAAACTTGAAAACCTCACCATCTCGCAGAACAACCTCACCGGCGAACTTCCCAAGGA\
GCTCGCCGCCCTCACTTCCCTCAAGCACCTCAACATCTCTCACAACGTCTTCTCCGGCTATTTTCCCGGC\
AAAATAATTCTTCCGATGACCGAACTCGAGGTCCTCGACGTCTACGACAACAACTTCACCGGATCGCTTC\
CGGAAGAGTTCGTGAAACTGGAGAAATTGAAATACCTGAAGCTCGACGGAAACTATTTCTCCGGAAGCAT\
ACCGGAGAGTTACTCGGAGTTTAAGAGCTTGGAGTTTTTAAGCTTAAGCACCAATAGCTTATCGGGGAAT\
ATTCCGAAGAGTTTGTCTAAGTTGAAGACGCTGAGGATTCTCAAGCTCGGATACAACAACGCTTACGAAG\
GCGGAATTCCACCGGAGTTCGGCACCATGGAATCTCTGAAATACCTTGACCTCTCAAGCTGCAACCTCAG\
CGGCGAGATTCCACCGAGTCTAGCAAATATGAGAAACCTCGACACGTTGTTCTTGCAAATGAATAACCTC\
ACCGGAACCATTCCGTCTGAGCTCTCCGACATGGTGAGCCTCATGTCACTGGATCTCTCCTTCAACGGCC\
TCA 

Based on the blastx results, what is the likely function of the query sequence?
Does it contain a coding region? Does it code for a complete gene? Or does it just code for a part of a gene?



4. tblastn - to search in a nucleotide sequence database with a protein query sequence

Use this protein sequence to find out about whether it might be possible to trace the organism it came from:\
\>CAE7832393\
MQLFQQLGEALERLSSGHCAWNDLTKAELRNLAEFNEEPKSAIEGLEGLALEYTWQELHQATDGFSTARQ\
LGSGASGTVYHATLCEGTEAAVKVLDAPLRGGFEDEVRLLSRCRHPNVVMLLGFAEESLCSVFRHRRCAL\
VYELLHGGDLYRRLQASRAYLWHERLRTATEVCRGLAHLHKHRPKIFHRDIKSQNILFSSDGTAKIADFG\
LACMAADNDVHEMATSQVAGTVGYSDPLYTRTGVMSESSECYSFGQVLIEILVGRPPAVLAQDGHSCVFL\
SDELRPREDRAKSRVLSRLDKRAQWPLCTAAGLSTLALLCIHEDADRRPTFLEATDMLRDLTAAAFVQEA\
DQDSVGRDPTEQPETCHHTVPLVRAHGILEPGREDSTAGCQGSPENALRQPELPQLESAEVLGHFLQHAQ\
HARQLTGQPRQAQILSPSPNFPHAKASLHQAQLQVQHRQSPVPVQHQQTQALSPGAVMQLSPTALQVWQP\
HSPGHGPNAPSPPPPLQLLQVAACPRPINRPCGPIGPMSPRDLRTSHAKSMHDIQAESNRINICLRASSL\
AAPALVGDRQPPGAEEASELRSESV

Based on the tblastn results, what can we say about the organism that it might have come from and which chromosome it came from.

5. tblastx - to search in a nucleotide database (each nucleotide sequence is converted to 6 possible protein sequences corresponding to the various reading frames) using a query nucleotide sequence which is also converted to its six possible protein sequences.

Use this nucleotide sequence to search for all known organisms that may have similar genes or parts of proteins:\
\>NM_001344809\
CATTCTCTTCTCTCTCTTTATCTGACTCTCTCTTATCTCCACTGTTCCCAAGCCCATACGGGCAAAAGAA\
CCTGCTCCCAAAGTTGGCTCTGCAACAGAACAGAACTCTTAATTGTAGTAACACTAATGTATCCACTCAC\
AGTCTCACAGTTTCCAACTCTCCTCAAACACCATCTTAAACTTGACTTCTCTTCTACTTCTCATCTTCAC\
ACTTGCCCTTTTAAACTCATCCTCTCAAGCCCACAACACTCACATTCTCTTTCTCTCCCTCTCGGTCTTC\
AGCTCAAGATAACATAGAATGGAAGATCATTACCATCAAGTAGAAGTGGAGGGAGAAGAAGAGATCAAGC\
CAAGCAAAGAAGCCAACAAGACAGACGAAAACACATCATCATTAAGAATATTCCCCTGCCTCTTTTGTTC\
TAGAAAGTTCCATAGCTCCCAAGCCCTAGGAGGCCACCAGAACGCCCACAAGAAGGAGCGAACCGCTGCT\
AGAAGAGCCAAAAGGGCTTATGATTTTGTCAACAACAATGACTTCCTTCACACGTTACCTGTTTTCTTAT\
CCTCTCCCTCTCAACATCACTTGACCATCTTAGGCTACCCTGCTTCTGCCTCCGTTGCCTGTTTTCCGAC\
GGTTCATCCCGACCATCCGATTTTCAAATCCAGTGGTTCTCATGTCGTGTTGGCTACATCCCACCAAGGT\
AGAGATTGCAAAGGAGGGTACTGTTGTCAACAACGTGTAGACATTTTGGATCATCATTATAACGTGGTCA\
ATAGTGACAAGGGTAAAGATCAGTGTCTTGATCTCTCCCTACATTTGTGATTTTAGCATTATCATTTGTT\
AGTTATGGTCTTGCCAAAATTGACTACAAACTGTTCCATCCGTATCCTGATTTTAATTGGTATTCCGAGA\
AATAATGGACGATATATAGTGATTAAACTATTTGTAATTCTTT

What can we say about the organisms that have this?

As far as strategies for searching for information about nucleotide or protein sequences go:
1. Nucleotide databases like the ones in GenBank are enormous and so blastn has to do a lot of work unless we focus on specific nucleotide databases. blastn itself is really fast because we only have (for the most part) 4 nucleotides! There are other "letters" to signify various combinations of the 4 nucleotides.
2. Among the many parameters for blastn are ones that will make blastn search for highly similar sequences (megablast) or more dissimilar sequences (discontiguous megablast) or the "default" search which looks for "somewhat similar" sequences.
3. tblastx, on the other hand, is a very expensive search strategy since we are looking at "every" nucleotide sequence converted to 6 protein sequences (the 6 reading frames!).
4. However, sometimes, tblastx is the best option if we want to find sequences that have diverged because of evolution. Assuming that protein function is mostly preserved through evolution, we can say that amino acid (protein) sequences are more likely to be preserved than nucleotide sequences since there is redundancy in the information in codons (64 possible codons for 20 amino acids). This means that two species that have very different DNA (or RNA) sequences can end up giving us very similar protein sequences!
5. Using tblastx for non-coding DNA really does not make much sense. It really is meant for protein coding genes.
