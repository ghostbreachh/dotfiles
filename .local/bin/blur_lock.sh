#!/bin/bash
# High-End Blurred Lockscreen with Jarvis-style TUI interface

# Ensure key grabs and socket issues are settled
sleep 0.1

# Themed deep-purple solid color fallback
THEME_BG="09050e"

# Create a temporary blurred wallpaper
if maim /tmp/screen.png 2>/dev/null; then
    # Heavy frosted-glass blur (scale down to 10%, heavy blur, scale back up)
    if magick /tmp/screen.png -resize 10% -blur 0x16 -resize 1000% /tmp/screen.png 2>/dev/null; then
        # Launch i3lock-color with bottom-left clock and centered indicator
        i3lock \
          -i /tmp/screen.png \
          --clock \
          --indicator \
          --time-str="%H:%M" \
          --date-str="%A, %B %d" \
          --inside-color=05020990 \
          --ring-color=9f52f0ff \
          --line-color=00000000 \
          --keyhl-color=00e5ffff \
          --bshl-color=ff1744ff \
          --separator-color=00000000 \
          --insidever-color=050209c0 \
          --ringver-color=00e5ffff \
          --insidewrong-color=050209c0 \
          --ringwrong-color=ff1744ff \
          --verif-text="DECRYPTING..." \
          --wrong-text="ACCESS DENIED" \
          --time-color=ebd9fcff \
          --date-color=a38db8ff \
          --verif-color=00e5ffff \
          --wrong-color=ff1744ff \
          --time-font="FiraCode Nerd Font" \
          --date-font="FiraCode Nerd Font" \
          --verif-font="FiraCode Nerd Font" \
          --wrong-font="FiraCode Nerd Font" \
          --greeter-text="ACCESS RESTRICTED: UMAR" \
          --greeter-color=a38db8ff \
          --greeter-font="FiraCode Nerd Font" \
          --greeter-size=14 \
          --time-size=44 \
          --date-size=14 \
          --verif-size=14 \
          --wrong-size=14 \
          --time-pos="80:h-120" \
          --date-pos="80:h-80" \
          --greeter-pos="80:h-160" \
          --time-align=1 \
          --date-align=1 \
          --greeter-align=1 || i3lock -c "$THEME_BG"
    else
        # Fallback to solid color if conversion failed
        i3lock -c "$THEME_BG"
    fi
    # Clean up immediately after unlocking
    rm -f /tmp/screen.png
else
    # Fallback to solid color if capture failed
    i3lock -c "$THEME_BG"
fi
