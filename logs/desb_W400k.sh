#!/bin/bash
cd "$(dirname "$0")/.."
for s in static dynamic guided; do ./lab12 desbalance $s 400000 > resultados/repeticiones/desb_${s}_W400000.csv 2>/dev/null; done
