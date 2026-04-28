from Bio import SeqIO

files = {
    "p1": "data/p1.fasta",
    "p3": "data/p3.fasta",
    "p12": "data/p12.fasta"
}

def is_phi6(desc):
    desc = desc.lower()
    return ("phi-6" in desc) or ("phi6" in desc)

for gene, file in files.items():
    out_file = f"data/{gene}_clean.fasta"
    records = []

    for record in SeqIO.parse(file, "fasta"):

        # keep only phi6-related sequences
        if not is_phi6(record.description):
            continue

        # simplify header
        record.id = record.id.split()[0]
        record.description = gene

        records.append(record)

    SeqIO.write(records, out_file, "fasta")

print("Cleaning complete")
