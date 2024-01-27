# open the .txt file and extract data from it.
with open("./Data_file.txt") as Data_file:
    Data = Data_file.readline()
Protein_seq = Data.strip()
print("The given protein sequence is:", Protein_seq, sep="\n")
# open the .txt file and extract data from it.
# this step is important to build a dictionary contains the mass for each amino acid.
with open("./Data_file2.txt") as Data_file:
    aa_masses = Data_file.readlines()
Mass_dict = dict()
for aa in range(len(aa_masses)):
    Mass_dict[aa_masses[aa][0]] = float(aa_masses[aa][4:])
print("The mass for each amino acid in dalton(Da):", Mass_dict, sep='\n')
total_protein_mass = 0
for aa in Protein_seq:
    total_protein_mass += Mass_dict[aa.upper()]
print("The given protein sequence mass is: {} Da = {} kDa".format(round(total_protein_mass, 4),
                                                                  round(total_protein_mass / 1000, 4)))