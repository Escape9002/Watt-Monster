#! /bin/bash

gateway="192.168.0.2"

ip route add 10.0.0.0/24 via $gateway
ip route add 10.6.6.0/24 via $gateway
ip route add 10.9.9.0/24 via $gateway
