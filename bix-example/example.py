from Bio.PDB import PDBParser

p = PDBParser(QUIET=True)
s = p.get_structure('3mxw.pdb', '3mxw.pdb')

n_c = len(list(s.get_chains()))

print(f"This protein has {n_c} chains")
