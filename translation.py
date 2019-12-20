gencode = {
'ATA':'I', 'ATC':'I',
'ACA':'T', 'ACC':'T',
'AAC':'N', 'AAT':'N',
'AGC':'S', 'AGT':'S',
'CTA':'L', 'CTC':'L',
'CCA':'P', 'CCC':'P',
'CAC':'H', 'CAT':'H',
'CGA':'R', 'CGC':'R',
'GTA':'V', 'GTC':'V',
'GCA':'A', 'GCC':'A',
'GAC':'D', 'GAT':'D',
'GGA':'G', 'GGC':'G',
'TCA':'S', 'TCC':'S',
'TTC':'F', 'TTT':'F',
'TAC':'Y', 'TAT':'Y',
'TGC':'C', 'TGT':'C',
'ATT':'I',
'ACG':'T',
'AAA':'K',
'AGA':'R',
'CTG':'L',
'CCG':'P',
'CAA':'Q',
'CGG':'R',
'GTG':'V',
'GCG':'A',
'GAA':'E',
'GGG':'G',
'TCG':'S',
'TTA':'L',
'TAA':'_',
'TGA':'_',
'ATG':'M',
'ACT':'T',
'AAG':'K',
'AGG':'R',
'CTT':'L',
'CCT':'P',
'CAG':'Q',
'CGT':'R',
'GTT':'V',
'GCT':'A',
'GAG':'E',
'GGT':'G',
'TCT':'S',
'TTG':'L',
'TAG':'_',
'TGG':'W'}
dna1 = "AATGATCGATCGTACGCTG"
protien =""
last_codon=len(dna1)-2
for dash in range(0,last_codon ,3):
    codon=dna1[dash:dash+3]
    aa= gencode.get(codon)
   
    print ("codon is ", codon)
    print ("amino acid is",aa)
    protien=protien+aa

    print ("protien sequance is ",protien)
    
