#!/bin/bash
cd "$(dirname "$0")/.."
for s in static dynamic guided; do for i in 1 2; do ./lab12 desbalance $s > resultados/repeticiones/desb_${s}_rep$i.csv 2>/dev/null; done; done
