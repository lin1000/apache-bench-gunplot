#!/bin/sh

# Output Keepalived server role
echo "========== KEEPALIVED_ROLE: ${KEEPALIVED_ROLE}"

# Start Keepalived
/usr/local/keepalived/sbin/keepalived -n -l -D -f "/data/etc/keepalived/keepalived-${KEEPALIVED_ROLE}.conf" --dont-fork --log-console