#!/bin/bash
# Ejecuta los 10 experimentos del lab 12 en orden. CSV -> resultados/, stderr -> logs/
set -e
cd "$(dirname "$0")/.."
for fp in 1.00 0.95 0.90 0.75 0.50; do
  n=$(echo $fp | tr -d '.')
  echo "== amdahl fp=$fp"; ./lab12 amdahl 400000 $fp > resultados/amdahl_fp$n.csv 2> logs/amdahl_fp$n.err
done
echo "== suma";               ./lab12 suma > resultados/suma.csv 2> logs/suma.err
for s in static dynamic guided; do
  echo "== desbalance $s";    ./lab12 desbalance $s > resultados/desb_$s.csv 2> logs/desb_$s.err
done
echo "== gustafson";          ./lab12 gustafson > resultados/gustafson.csv 2> logs/gustafson.err
echo TERMINADO
