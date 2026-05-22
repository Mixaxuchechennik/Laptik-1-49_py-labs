import sys

data = sys.stdin.read().splitlines()

dna = "".join(data[1:])

if len(dna) > 1000:
    dna = dna[:1000]

complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

for i in range(len(dna)):
    for length in range(4, 13):
        if i + length <= len(dna):
            sub = dna[i:i + length]

            rev_comp = "".join(complement[base] for base in reversed(sub))

            if sub == rev_comp:
                print(f"{i + 1}, {length}.")
                