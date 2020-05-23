from Bio.PDB import PDBParser

p = PDBParser(QUIET=True)
s = p.get_structure('3mxw.pdb', '3mxw.pdb')

n_c = len(list(s.get_chains()))
n_h_r = len([ r for r in s[0]['H'] if r.resname != "HOH" ])

print(f"This protein has {n_c} chains and {n_h_r} residues in chain H")
