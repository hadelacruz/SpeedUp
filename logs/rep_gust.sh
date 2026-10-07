#!/bin/bash
cd "$(dirname "$0")/.."
for i in 1 2 3; do ./lab12 gustafson > resultados/repeticiones/gustafson_rep$i.csv 2>/dev/null; done
