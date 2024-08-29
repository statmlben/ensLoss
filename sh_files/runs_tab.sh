#!/bin/bash

## Tabular
for id_tmp in 4134 41159 41161 1039 41142 1128 1138 1166 1134 1130 1139 1161 1142 1146; do
    id="${id_tmp}"
    python main_tab.py -B=128 -e=300 -ID="$id" -N='TabMLP1' -R=10 --log
    python main_tab.py -B=128 -e=300 -ID="$id" -N='TabMLP3' -R=10 --log
    python main_tab.py -B=128 -e=300 -ID="$id" -N='TabMLP5' -R=10 --log

    done
done

# nohup bash ./runs_tab.sh >/dev/null 2>&1 &