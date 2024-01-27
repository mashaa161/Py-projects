# open the .txt file and extract data from it.
with open("./Data_file.txt") as Data_file:
    Data = Data_file.readline().strip()
# The sequence is long, so I will print only the first 500 bP of it
print("The first 500 bP of the DNA sequence are:\n", Data[0: 500], sep="")
# now I will define the dictionary which contains the RNA genetic code and their correspondent amino acids
genetic_code = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L", "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S", "UAU":"Y", "UAC":"Y",  "UAA":"", "UAG": "", "UGU":"C", "UGC":"C",  "UGA":"", "UGG":"W", "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L", "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P", "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q", "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R", "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M", "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T", "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K", "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R", "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V", "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A", "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E", "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}
# now the next code section will convert the mRNA sequence to its corresponding protein
protein_seq = ""
start = Data.find('AUG')  # the start codon in mRNA is AUG
if start != -1:
    while start+2 < len(Data):
        codon = Data[start:start+3]
        if codon == "UAG" or codon == "UAA" or codon == "UGA":    # the stop codons in mRNA are UAG, UAA, and UGA
            break
        protein_seq += genetic_code[codon]
        start += 3
# write out the result protein sequence
print("The protein sequence for this mRNA sequence is:\n", protein_seq, sep="")
