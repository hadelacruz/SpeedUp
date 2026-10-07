import csv,sys
from collections import defaultdict
r=list(csv.DictReader(open(sys.argv[1])))
d=defaultdict(dict); ts={}
for x in r:
    n=int(x['N']); d[n][int(x['p'])]=float(x['t_seq'])/float(x['t_par']); ts[n]=float(x['t_seq'])/n*1e9
for n,v in d.items(): print(f"{n*8//1024:>7} KB ts={ts[n]:.3f}ns/el", ' '.join(f"p{p}:S={s:.2f}" for p,s in v.items()))
