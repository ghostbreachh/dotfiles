#!/bin/sh
# Wrapper for i3status to add custom indicators

i3status | while read -r line; do
    if pgrep -x redshift >/dev/null; then
        echo " 󰛨  Night | $line"
    else
        echo " 󰛩  Day | $line"
    fi
done
