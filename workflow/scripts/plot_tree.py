import sys
import os

# FORCE headless rendering (critical fix)
os.environ["QT_QPA_PLATFORM"] = "offscreen"

from ete3 import Tree, TreeStyle

tree_file = sys.argv[1]
output_file = sys.argv[2]

t = Tree(tree_file)

ts = TreeStyle()
ts.show_leaf_name = True
ts.show_branch_length = True
ts.show_branch_support = True
ts.scale = 50

t.render(output_file, tree_style=ts)