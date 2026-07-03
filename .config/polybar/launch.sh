#!/usr/bin/env bash

# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# Launch the single main bar with correct user session environment
export DISPLAY=${DISPLAY:-:0}
if [ "$XDG_RUNTIME_DIR" = "/run/user/0" ] || [ -z "$XDG_RUNTIME_DIR" ]; then
    export XDG_RUNTIME_DIR="/run/user/1000"
fi
if [ -z "$DBUS_SESSION_BUS_ADDRESS" ] || [[ "$DBUS_SESSION_BUS_ADDRESS" == *"/run/user/0"* ]]; then
    export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus"
fi

polybar main -c ~/.config/polybar/config.ini &

