#!/usr/bin/env bash

# creation of the script file from a basic one
DAY=$(date | cut -d " " -f 3)
sed 's/##/'$DAY'/g' template.py > $(echo $DAY)a.py
chmod +x $(echo $DAY)a.py

# creation of the data file

COOKIECODE=$(cat ~/cookiecode.txt |sed 's/\n//g')
#curl 'http://adventofcode.com/2017/day/'$(echo $DAY)'/input' -H "$(echo $COOKIECODE)" > $(echo $DAY)a_data.txt

xdg-open http://adventofcode.com/2017/day/$(echo $DAY)

tmux new-window -c "#{pane_current_path}" 'bash --init-file <(echo "vim ./'$(echo $DAY)'a.py")'
tmux split-window -v -p 30 -c "#{pane_current_path}" 'bash --init-file <(echo "watch -n1 ./'$(echo $DAY)'a.py")'
tmux select-pane -U
