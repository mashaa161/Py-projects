
# open the .txt file and extract data from it.
with open("./data_file.txt") as Data_file:
    Data = Data_file.readlines()
DNA_seq = Data[0].strip().upper()
motif = Data[1].strip().upper()
print("The DNA sequence is:\n", DNA_seq,"\nThe motif sequence is:\n", motif, sep="")
# this function will find all 
def locations(DNA, motif):
    ln_DNA = len(DNA)
    ln_motif = len(motif)
    loc_list = list()
    for nuc in range(ln_DNA - ln_motif + 1):
        if DNA[nuc: nuc + ln_motif] == motif:
            loc_list.append(nuc + 1)
    return loc_list
# write out the starting locations of the motif sequence in the DNA sequence
result = locations(DNA_seq, motif)
print("The locations of motif in DNA sequence are:\n", *result)