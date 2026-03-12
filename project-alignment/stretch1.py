from alignment import align

def parse_fasta(filename):
    sequences = {}
    with open(filename) as f:
        lines = f.readlines()
    for i in range(0, len(lines), 2):
        metadata = lines[i].strip()
        sequence = lines[i + 1].strip()
        species_tag = metadata.split("_")[1]
        sequences[species_tag] = sequence
    return sequences

species_map = {
    "hg38":     "Human",
    "panTro4":  "Chimp",
    "rheMac3":  "Rhesus macaque",
    "canFam3":  "Dog",
    "rn5":      "Rat",
    "mm10":     "Mouse",
    "unknown":  "Unknown suspect",
}

sequences = parse_fasta("lct_exon8.txt")
unknown_seq = sequences["unknown"]

best_match = None
best_score = float("inf")  #because every subsequent value that's better needs to be smaller.

for tag, seq in sequences.items():
    if tag == "unknown":
        continue
    score, _, _ = align(unknown_seq, seq)
    print(f"{species_map[tag]}: score = {score}")
    if score < best_score:
        best_score = score
        best_match = tag

print(f"\nClosest match: {species_map[best_match]} (score: {best_score})")