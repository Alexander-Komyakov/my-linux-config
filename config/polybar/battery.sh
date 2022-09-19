#!/usr/bin/bash

echo "bat" $(cat /sys/class/power_supply/BAT1/capacity)"% " $(cat /sys/class/power_supply/BAT1/status) | tr '[:upper:]' '[:lower:]'
