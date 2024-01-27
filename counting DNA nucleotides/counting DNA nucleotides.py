# open the .txt file and extract data from it.
with open("./Data_file.txt") as Data_file:
    Data = Data_file.readline().strip()
print(Data)
# counting the number of evey nucleotide in DNA sequence
def count(DNA_seq):
    Nuc_counts = dict(A = 0, C = 0, G = 0, T = 0)
    for nuc in DNA_seq:
        Nuc_counts[nuc] += 1
    return Nuc_counts
# print nucleotides counts in DNA string
nuc_counts = count(Data)
for nuc_type in nuc_counts.keys():
    print(nuc_type, ": ", nuc_counts[nuc_type], sep="")