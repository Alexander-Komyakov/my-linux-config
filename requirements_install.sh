#!/bin/bash


sudo pacman -S imagemagick qtile i3lock picom xorg-setxkbmap vim xfce4-terminal git parcellite --noconfirm

path_to_file=$(dirname $0)
cp $path_to_file/config/qtile/config.py ~/.config/qtile/config.py
cp $path_to_file/config/qtile/autostart.sh ~/.config/qtile/autostart.sh
cp $path_to_file/config/qtile/keyboard.sh ~/.config/qtile/keyboard.sh
cp $path_to_file/.vimrc ~/.vimrc
cp $path_to_file/.bashrc ~/.bashrc
cp $path_to_file/.xinitrc ~/.xinitrc
cp $path_to_file/.Xmodmap ~/.Xmodmap
cp $path_to_file/config/xfce4/terminal/terminalrc ~/.config/xfce4/terminal/terminalrc

git clone https://aur.archlinux.org/yay-git.git && cd yay-git
exec makepkg -si --noconfirm
cd .. && rm -rf yay-git
sudo pacman -S sddm --noconfirm
yay -S archlinux-themes-sddm --noconfirm
echo "[Theme]
Current=materia-dark" | sudo tee /etc/sddm.conf
sudo systemctl enable --now sddm
