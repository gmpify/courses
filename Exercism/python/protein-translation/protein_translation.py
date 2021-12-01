PROTEIN_DICT = {
    'AUG': 'Methionine',
    'UUU': 'Phenylalanine',
    'UUC': 'Phenylalanine',
    'UUA': 'Leucine',
    'UUG': 'Leucine',
    'UCU': 'Serine',
    'UCC': 'Serine',
    'UCA': 'Serine',
    'UCG': 'Serine',
    'UAU': 'Tyrosine',
    'UAC': 'Tyrosine',
    'UGU': 'Cysteine',
    'UGC': 'Cysteine',
    'UGG': 'Tryptophan'
}

STOP_CODONS = ['UAA', 'UAG', 'UGA']

def proteins(strand):
    codons = [strand[i:i+3] for i in range(0, len(strand), 3)]

    proteins = []
    for c in codons:
        if c in STOP_CODONS:
            break
        proteins.append(PROTEIN_DICT[c])

    return proteins
