def complement(DNA):
    comp = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    compDNA = ''
    for b in DNA:
        compDNA += comp[b]
        return compDNA

def reverse(DNA):
    return DNA[::-1]

def reverse_complement(DNA):
    compDNA = complement(DNA)
    revCompDNA = reverse(compDNA)
    return revCompDNA
 
DNA = input("Please enter a DNA sequence. ")
revCompDNA = reverse_complement(DNA)
print("You have entered: '%s'" % (DNA))
print("The reverse comp: '%s'" % (revCompDNA))
