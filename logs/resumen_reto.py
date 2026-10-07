"""Resumen del reto: speedup a 64 KB (p=2 y p=4) en cada una de las 5 corridas guardadas."""
import csv, statistics
S = {2: [], 4: []}
print("Reto - speedup con arreglo de 64 KB (5 corridas completas de ./lab12 reto)")
for i in range(1, 6):
    f = f"resultados/reto/reto_corrida{i}.csv"
    fila = {int(x["p"]): float(x["t_seq"]) / float(x["t_par"]) for x in csv.DictReader(open(f)) if int(x["N"]) == 8192}
    for p in (2, 4): S[p].append(fila[p])
    print(f"corrida {i}: p=2 -> S={fila[2]:.2f} ({'> 2' if fila[2] > 2 else '<= 2'})   p=4 -> S={fila[4]:.2f} ({'> 4' if fila[4] > 4 else '<= 4'})")
for p in (2, 4):
    print(f"mediana p={p}: S={statistics.median(S[p]):.2f}   S>p en {sum(x > p for x in S[p])} de 5 corridas")
