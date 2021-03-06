#!/bin/bash

# Authenticate via wpa_supplicant and config instead of network manager

interface=$1

if [[ $UID -gt 0 ]];
then
    echo "[X] Must run script as root!"
    exit 1
fi

# if no arg passed, use default interface name
if [[ $interface == '' ]];
then
    # my default interface... deal with it, my script
    interface='wlp2s0b1'
fi

echo "[**] Turning off networking, the network manager"

# Turn off network manager, networking and bring down interfaces
service network-manager stop
ifconfig $interface down
service networking stop
sleep 2

# if no supplicant file, warn user and exit
if [[ ! -e "/etc/wpa_supplicant.conf" ]];
then
    echo "[X] wpa_supplicant config not found, /etc/wpa_supplicant.conf"
    exit 1
fi

echo "[**] Connecting via wpa_supplicant with set configurations"
wpa_supplicant -Dnl80211 -i$interface -c/etc/wpa_supplicant.conf -B
