#!/bin/bash
cd "$(dirname "$0")/.."
for i in 1 2 3; do ./lab12 amdahl 400000 1.00 > resultados/repeticiones/amdahl_fp100_rep$i.csv 2>/dev/null; done
