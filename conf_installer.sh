#!/bin/bash


dp_env=$1
path_to_file="${0%/*}"
mkdir -p ~/.config/xfce4/terminal/
cp "$path_to_file/.vimrc" ~/.vimrc
cp "$path_to_file/.bashrc" ~/.bashrc
cp "$path_to_file/.xinitrc" ~/.xinitrc
cp "$path_to_file/.Xmodmap" ~/.Xmodmap
cp "$path_to_file/config/xfce4/terminal/terminalrc" ~/.config/xfce4/terminal/terminalrc

sudo pacman -Sy

yayb=`pacman -Qs | grep yay`
if [ -z "$yayb" ]; then
	git clone https://aur.archlinux.org/yay-git.git && cd yay-git
	exec makepkg -si --noconfirm
	cd .. && rm -rf yay-git
fi

sudo pacman -S imagemagick i3lock picom xorg\
	xorg-setxkbmap vim xfce4-terminal git parcellite --noconfirm

if [[ "$dp_env" == "qtile" ]]; then
	sudo pacman -S qtile --noconfirm
	cp "$path_to_file"/config/qtile/config.py ~/.config/qtile/
	cp "$path_to_file"/config/qtile/autostart.sh ~/.config/qtile/
	cp "$path_to_file"/config/qtile/keyboard.sh ~/.config/qtile/
elif [[ "$dp_env" == "i3" ]]; then
	sudo pacman -S dmenu i3-gaps feh polybar --noconfirm
	yay -S i3lock-multimonitor --noconfirm
	cp "$path_to_file"/config/i3/config ~/.config/i3/
	cp "$path_to_file"/config/polybar/config.ini ~/.config/polybar/
	cp "$path_to_file"/config/polybar/launch.ini ~/.config/polybar/
fi


sudo pacman -S sddm --noconfirm
yay -S archlinux-themes-sddm --noconfirm
echo "[Theme]
Current=materia-dark" | sudo tee /etc/sddm.conf
sudo systemctl enable --now sddm
