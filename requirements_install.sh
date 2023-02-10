#!/bin/bash


sudo pacman -S imagemagick qtile i3lock picom xorg-setxkbmap rxvt-unicode vim

path_to_file=$(dirname $0)
cp $path_to_file/config/qtile/config.py ~/.config/qtile/config.py
cp $path_to_file/config/qtile/autostart.sh ~/.config/qtile/autostart.sh
cp $path_to_file/.vimrc ~/.vimrc
cp $path_to_file/.bashrc ~/.bashrc
cp $path_to_file/.xinitrc ~/.xinitrc
cp $path_to_file/.Xresources ~/.Xresources
xrdb ~/.Xresources
