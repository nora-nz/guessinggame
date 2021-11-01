# nora-projects
These are all my projects using Python 3. 
Rosalind_GC_content.py takes in a file containing FASTA format tags associated with nucleotide sequences. I used RegEx to separate tags from sequences and order them into key-value pairs. The percentage of G and C nucleotides is then calculated, compared and the tag of the highest percentage sequence is returned. 

Rosalind_Hamming_distance.py compares two nucleotide sequences and returns how many differences there are between - also called the Hamming distance.

Rosalind_Recurrence_relations.py returns the final item of a sequence based on the number of recurrences and a rate defining coefficient in the context of rabbit populations. In a challenge I am currently working on the logistic map is further complicated by an additional coefficient.

Rosalind_Translate_RNA_into_protein.py translates nucleotide codons into an amino acid sequence. I used a dictionary which contains codons as keys and single letter amino acid codes as values. The stop codons insert a space instead of "Stop". A potential improvement for the future could be to only start an amino acid sequence if a methionine residue is found.

The "guessing game" file is the first program I made after a beginner Python course. It is an interactive game where the program scans the user's input, compares it with a dictionary and returns yes/no values if the user's guess is an attribute of the object of the current round.
