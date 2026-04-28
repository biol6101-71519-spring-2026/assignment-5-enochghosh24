from Bio import Phylo

tree_files = snakemake.input
output_file = snakemake.output[0]

with open(output_file, "w") as out:
    out.write("Tree comparison (simple RF-like distance)\n\n")

    for i in range(len(tree_files)):
        for j in range(i+1, len(tree_files)):
            t1 = Phylo.read(tree_files[i], "newick")
            t2 = Phylo.read(tree_files[j], "newick")

            leaves1 = set(x.name for x in t1.get_terminals())
            leaves2 = set(x.name for x in t2.get_terminals())

            diff = len(leaves1.symmetric_difference(leaves2))

            out.write(f"{tree_files[i]} vs {tree_files[j]}: {diff}\n")