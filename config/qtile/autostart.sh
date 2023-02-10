#!/usr/bin/bash

exec setxkbmap -layout 'us,ru' -option 'grp:caps_toggle' &
exec picom &
exec xrdb -merge "$userresources" &
exec xset s off &
exec xset dpms 0 0 0 &
exec xset r rate 200 25 &
