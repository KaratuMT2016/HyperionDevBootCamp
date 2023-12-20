dna = 'atcgctagctag'

upper_seq = dna.upper()

replace_sqe = upper_seq.replace('A', 'T')

print(dna)
print(upper_seq)
print(replace_sqe)

trait_seqgen_seq = 'TCGA'

if gen_seq in upper_seq:
    print(f"Genetic marker located: {gen_seq}")

segment = upper_seq.split('G')

print(f"Segment split by G : {segment}")


trait_seq = 'TAG'

if trait_seq in segment:
    print(f"Genetic marker located: {trait_seq}")