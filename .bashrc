#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

force_color_promt=yes
alias ls='ls --color=auto'
PS1='\[\e[33m\]\u\[\e[31m\]@\[\e[32m\]\h:\W\[\e[37m\]$ '
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
