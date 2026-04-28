from ete3 import Tree
import itertools

trees = {
    "species": snakemake.input.species_tree,
    "concat": snakemake.input.concat_tree,
}

# add gene trees dynamically
for i, path in enumerate(snakemake.input.gene_trees):
    trees[f"gene{i+1}"] = path

loaded = {name: Tree(path) for name, path in trees.items()}

results = []

for (n1, t1), (n2, t2) in itertools.combinations(loaded.items(), 2):
    rf, max_rf, *_ = t1.robinson_foulds(t2, unrooted_trees=True)
    norm_rf = rf / max_rf if max_rf != 0 else 0
    results.append(f"{n1}\t{n2}\t{rf}\t{max_rf}\t{norm_rf:.4f}")

# ✅ ONLY ONE OUTPUT
with open(snakemake.output[0], "w") as f:
    f.write("tree1\ttree2\trf\tmax_rf\tnorm_rf\n")
    f.write("\n".join(results))