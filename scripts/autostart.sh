#!/bin/bash

wall="wall-snow-mountain.jpeg"

feh --bg-scale /home/don/Pictures/Wallpapers/$wall &
picom --config /home/don/.config/picom/picom.conf &
dunst --config /home/don/.config/dunst/dunstrc &
