# open the .txt file and extract data from it.
with open("./Data_file.txt") as Data_file:
    Data = Data_file.readline().strip()
print(Data)
#tnscribing DNA into RNA
def DNA2RNA(DNA_seq):
    RNA = " "
    for nuc in DNA_seq:
        if nuc.upper() == "T":
            RNA += "U"
        else:
            RNA += nuc
    return RNA
print(DNA2RNA(Data))