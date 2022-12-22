#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '
export fish_greeting=""
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
#source ~/.local/bin/virtualenvwrapper.sh
export Electronintorg="5626936568:AAGPWJph_gs-_KNkJQrx1JfvyMkalCb775c"
#export ElectronintorgBot="5626936568:AAGPWJph_gs-_KNkJQrx1JfvyMkalCb775c"
export gitHub="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"
exec fish
