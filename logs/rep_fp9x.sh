#!/bin/bash
cd "$(dirname "$0")/.."
for fp in 0.95 0.90; do for i in 1 2; do
 n=$(echo $fp | tr -d '.'); ./lab12 amdahl 400000 $fp > resultados/repeticiones/amdahl_fp${n}_rep$i.csv 2>/dev/null; done; done
