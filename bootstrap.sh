#!/usr/bin/env bash
# Majestic Purple & Black i3wm Rice Bootstrap Script

set -euo pipefail

# Style formatting helper tokens
RED='\033[0;31m'
GREEN='\033[0;32m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "${PURPLE}"
echo "    ██████╗  ██████╗ ████████╗███████╗██╗██╗     ███████╗███████╗"
echo "    ██╔══██╗██╔═══██╗╚══██╔══╝██╔════╝██║██║     ██╔════╝██╔════╝"
echo "    ██║  ██║██║   ██║   ██║   █████╗  ██║██║     █████╗  ███████╗"
echo "    ██║  ██║██║   ██║   ██║   ██╔══╝  ██║██║     ██╔══╝  ╚════██║"
echo "    ██████╔╝╚██████╔╝   ██║   ██║     ██║███████╗███████╗███████║"
echo "    ╚═════╝  ╚═════╝    ╚═╝   ╚═╝     ╚═╝╚══════╝╚══════╝╚══════╝"
echo -e "         --- Majestic Purple & Black Desktop Installer ---${NC}\n"

# Verify dependencies
dependencies=(i3-wm polybar alacritty picom rofi dunst fastfetch feh redshift maim xclip xdotool)
missing_deps=()

echo -e "${CYAN}[*] Verifying system dependencies...${NC}"
for dep in "${dependencies[@]}"; do
    if ! command -v "$dep" &>/dev/null; then
        missing_deps+=("$dep")
    fi
done

if [ ${#missing_deps[@]} -ne 0 ]; then
    echo -e "${RED}[!] Missing packages detected: ${missing_deps[*]}${NC}"
    echo -e "    Please install them via pacman: sudo pacman -S ${missing_deps[*]}"
else
    echo -e "${GREEN}[✔] All system dependencies verified.${NC}"
fi

# Define directories
CONFIG_DIR="$HOME/.config"
BIN_DIR="$HOME/.local/bin"
DOTFILES_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Create local directories if missing
mkdir -p "$CONFIG_DIR"
mkdir -p "$BIN_DIR"

# Target config links/copies
configs=(i3 polybar alacritty picom rofi dunst fastfetch)

echo -e "\n${CYAN}[*] Setting up configuration directories under ~/.config...${NC}"
for conf in "${configs[@]}"; do
    target="$CONFIG_DIR/$conf"
    src="$DOTFILES_DIR/.config/$conf"
    
    if [ -d "$target" ] || [ -f "$target" ]; then
        echo -e "    [!] Backup existing path: $target -> ${target}.bak"
        rm -rf "${target}.bak"
        mv "$target" "${target}.bak"
    fi
    
    echo -e "    [+] Linking: $src -> $target"
    ln -sf "$src" "$target"
done

# Set up local scripts
echo -e "\n${CYAN}[*] Installing helper scripts under ~/.local/bin...${NC}"
scripts=(blur_lock.sh toggle_guides.py rice_firefox.py i3status_pill_wrapper.py i3status_wrapper.sh)
for script in "${scripts[@]}"; do
    target="$BIN_DIR/$script"
    src="$DOTFILES_DIR/.local/bin/$script"
    
    echo -e "    [+] Linking: $src -> $target"
    ln -sf "$src" "$target"
    
    echo -e "    [+] Setting executable permissions on $target"
    chmod +x "$target"
done

# Set up startpage
echo -e "\n${CYAN}[*] Linking user startpage...${NC}"
target_startpage="$HOME/startpage"
src_startpage="$DOTFILES_DIR/startpage"
if [ -d "$target_startpage" ]; then
    echo -e "    [!] Backup existing startpage: $target_startpage -> ${target_startpage}.bak"
    rm -rf "${target_startpage}.bak"
    mv "$target_startpage" "${target_startpage}.bak"
fi
ln -sf "$src_startpage" "$target_startpage"

# Check Nerd Font
echo -e "\n${CYAN}[*] Verifying font requirements...${NC}"
if fc-list : family | grep -iq "FiraCode"; then
    echo -e "${GREEN}[✔] FiraCode Nerd Font is installed.${NC}"
else
    echo -e "${RED}[!] FiraCode Nerd Font not found. Some icons may not render properly.${NC}"
    echo -e "    Please install ttf-firacode-nerd from Arch repos or AUR."
fi

echo -e "\n${GREEN}[✔] Installation completed successfully!${NC}"
echo -e "    Please reload your window manager using ${PURPLE}Mod+Shift+r${NC} to activate."
