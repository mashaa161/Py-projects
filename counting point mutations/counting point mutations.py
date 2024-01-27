# open the .txt file and extract data from it.
with open("./Data_file.txt") as Data_file:
    Data = Data_file.readlines()
first_seq = Data[0].strip()
second_seq = Data[1].strip()
print("First sequence:",first_seq, "Second sequence:", second_seq, sep="\n")
# calculate the hamming distance between these two DNA sequences
def H_d(seq1, seq2):
    hamm_dist = 0
    for nuc_order in range(len(seq1)):
        if seq1[nuc_order] != seq2[nuc_order]:
            hamm_dist += 1
    return hamm_dist
print("The hamming distance between the two DNA sequences is:", H_d(first_seq, second_seq))