#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

force_color_promt=yes
alias ls='ls --color=auto'
alias ll='ls --color=auto -al'
alias gosw='cd ~/.local/share/StartWine/data/scripts'
PS1='\[\e[33m\]\u\[\e[31m\]@\[\e[32m\]\h:\W\[\e[37m\]$ '
gitHub="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"
