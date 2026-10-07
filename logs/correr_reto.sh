#!/bin/bash
# Reto opcional: 5 corridas completas con un hilo por núcleo físico + 1 corrida del intento 1 (fork/join)
cd "$(dirname "$0")/../reto"
export OMP_PLACES=cores OMP_PROC_BIND=spread
for i in 1 2 3 4 5; do
  echo "reto corrida $i"; ./lab12 reto > ../resultados/reto/reto_corrida$i.csv 2>/dev/null
done
echo "reto_fj"; ./lab12 reto_fj > ../resultados/reto/reto_fj_corrida1.csv 2>/dev/null
echo RETO_TERMINADO
