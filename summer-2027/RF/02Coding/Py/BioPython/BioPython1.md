# Lab 1: Seq and SeqRecord Objects


## Learning Objectives
    - Understand Seq objects and their properties
    - Create and manipulate Seq objects
    - Learn SeqRecord objects and metadata handling
    - Perform basic sequence operations

The BioPython1.ipynb Python notebook should run as a Jupyter notebook.
So far it has been tested in:
- Google Colab

Here are some additional Python exercises you can try out using BioPython:

    # Create a protein SeqRecord
    protein_seq = Seq("MKVLWAALLVTFLAGCAKAKAVQVKVKALPDAQFEVVHSLAKWKRQTLGQHDFSAGEGLYTHMKALRPDEDRLSPLHSVYVDQWDWERVMGDGERQFSTLKSTVEAIWAGIKATEAAVSEEFGLAPFLPDQIHFVHSQELLSRYPDLDAKGRERAIAKDLGAVFLVGIGGKLSDGHRHDVRAPDYDDWSTPSELGHAGLNGDILVWNPVLEDAFELSSMGIRVDADTLKHQLALTGDEDRLELEWHQALLRGEMPQTIGGGIGQSRLTMLLLQLPHIGQVQAGVWPAAVRESVPSLL")
    protein_record = SeqRecord(
        seq=protein_seq,
        id="protein_001",
        name="sample_protein",
        description="A sample protein sequence"
    )
    print(f"Protein length: {len(protein_record.seq)} amino acids")

See if you can figure out how to do these:
    # Perform operations on a SeqRecord
    # Given a DNA sequence, create a SeqRecord and:
    # 1. Print the reverse complement
    # 2. Transcribe to RNA
    # 3. Add custom annotations


