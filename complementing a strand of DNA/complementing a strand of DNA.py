# open the .txt file and extract data from it.
with open("./Data_file.txt") as Data_file:
    Data = Data_file.readline().strip()
print(Data)
# create the reverse complement of DNA string
def rev_com(DNA_seq):
    seq1 = "ACGT"
    seq2 = "TGCA"
    pre_comp = str.maketrans(seq1, seq2)
    comp = DNA_seq.translate(pre_comp)
    rev_comp = comp[:: -1]
    return rev_comp
# print the reverse complement of the DNA sequence
print(rev_com(Data))