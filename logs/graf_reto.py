import csv, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from collections import defaultdict
S=defaultdict(lambda: defaultdict(list))
for i in range(1,6):
    for x in csv.DictReader(open(f'resultados/reto/reto_corrida{i}.csv')):
        S[int(x['p'])][int(x['N'])*8//1024].append(float(x['t_seq'])/float(x['t_par']))
fig,ax=plt.subplots(1,3,figsize=(12,4),sharey=False)
for a,p in zip(ax,(2,4,8)):
    ks=sorted(S[p]); med=[sorted(S[p][k])[2] for k in ks]
    a.fill_between(ks,[min(S[p][k]) for k in ks],[max(S[p][k]) for k in ks],alpha=.25,label='mín–máx (5 corridas)')
    a.plot(ks,med,'o-',label='mediana'); a.axhline(p,color='k',ls='--',lw=1,label=f'S = p = {p}')
    a.axvline(48,color='gray',ls=':',lw=1); a.set_xscale('log',base=2); a.set_title(f'p = {p}')
    a.set_xlabel('Tamaño del arreglo (KB, log)'); a.grid(alpha=.3,which='both')
ax[0].set_ylabel('Speedup S = Ts / Tp'); ax[0].legend(fontsize=8)
fig.suptitle('Reto: speedup vs tamaño del arreglo (línea punteada gris = L1d de 48 KB por núcleo)')
fig.tight_layout(); fig.savefig('graficas/reto_superlineal.png',dpi=150)
