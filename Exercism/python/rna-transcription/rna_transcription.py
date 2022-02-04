RNA_DICT = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U'
}

def to_rna(dna_strand):
    return ''.join(map(lambda x: RNA_DICT[x], dna_strand))
