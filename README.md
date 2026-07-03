# 🌌 Majestic Purple & Black i3wm Desktop Setup
[![WM: i3-gaps](https://img.shields.io/badge/WM-i3--gaps-blueviolet.svg?style=flat-square)](#)
[![Shell: Zsh / Bash](https://img.shields.io/badge/Shell-Zsh%20%2F%20Bash-darkviolet.svg?style=flat-square)](#)
[![Compositor: Picom](https://img.shields.io/badge/Compositor-Picom-purple.svg?style=flat-square)](#)
[![Terminal: Alacritty](https://img.shields.io/badge/Terminal-Alacritty-lavender.svg?style=flat-square)](#)

Welcome to the **Majestic Purple & Black** desktop environment customization ("rice"). This setup is a highly unified, glassmorphic visual workspace built for Arch Linux, optimized to deliver a fast, responsive, and gorgeous experience using tiling layouts and neon-accent indicators.

---

## 📸 Desktop Visuals & Gallery

Place your screenshots and showcase previews inside the `assets/` folder to populate this gallery:

| 💻 Full Desktop Overview | 💊 Floating Capsule Polybar |
| :---: | :---: |
| ![Desktop Overview](assets/desktop_preview.png) | ![Polybar Capsule](assets/bar_preview.png) |

| 🧼 Clean Workspace Gaps | 🔒 Frosted Glass Lockscreen |
| :---: | :---: |
| ![Clean Workspace](assets/clean_workspace.png) | ![Blur Lockscreen](assets/lockscreen_preview.png) |

---

## ✨ System Features & Modules

* **🧬 Consistent Theme Mapping:** Absolute color coordination across window borders, terminal schemes, app launchers, panels, notification bubbles, and Firefox CSS stylesheets.
* **💊 Floating Capsule Polybar:** Bottom-aligned capsule status bar featuring rounded contours and interactive modules. Left-clicking volume/battery widgets launches custom floating diagnostics menus.
* **📺 Frosted Glass Screen Locker:** Custom lockscreen script (`blur_lock.sh`) that captures screens, resizes to 10% to speed up ImageMagick blurs by 90%, and scales back to 100% with styled clock and security prompts.
* **📚 Cycle Cheatsheets Guide:** Cyclical guide popup (`toggle_guides.py`) that lists custom keyboard mappings and Neovim shortcuts inside a floating terminal window on keypress (`Mod+/`).
* **⚡ Compositor Power Tuning:** Customized Picom profile mapping with `xrender` backend optimization to prevent screen tearing on integrated graphics (e.g. Intel HD 3000) without high CPU load.
* **🦊 Riced Firefox Environment:** Custom `userChrome.css` stylesheet transforming standard browser tabs into floating, glowing purple pills, accompanied by a dynamic startpage with floating blurred animation blobs.

---

## 📁 Repository Directory Structure

```text
├── .config/
│   ├── i3/
│   │   └── config             # Core window manager rules & keybinds
│   ├── polybar/
│   │   ├── config.ini         # Floating bottom pill status bar configuration
│   │   └── launch.sh          # Handles multi-monitor bar setup and system d-bus envs
│   ├── alacritty/
│   │   └── alacritty.toml     # Opacity (0.92), padding (12x12), and colors
│   ├── picom/
│   │   └── picom.conf         # Performance-optimized compositor rules
│   ├── rofi/
│   │   └── config.rasi        # Glassmorphic application search launcher
│   ├── dunst/
│   │   └── dunstrc            # Rounded, glowing alert notification bubbles
│   └── fastfetch/
│       └── config.jsonc       # Customized terminal hardware specification output
├── .local/
│   └── bin/
│       ├── blur_lock.sh       # Frosted glass lockscreen script
│       ├── toggle_guides.py   # Cheat-sheet cycling controller script
│       └── rice_firefox.py    # Automatic Firefox style injector
├── startpage/
│   └── index.html             # CSS animated glassmorphic home startpage
├── bootstrap.sh               # Staging verification and symlink installer script
└── README.md                  # This file
```

---

## 🚀 Installation & Quickstart

### 1. Clone the Setup Repository
```bash
git clone https://github.com/yourusername/dotfiles.git ~/dotfiles
cd ~/dotfiles
```

### 2. Run the Staging Bootstrap Script
The script checks for package dependencies, verifies your Nerd Fonts, backs up existing configurations, and links directory folders:
```bash
./bootstrap.sh
```

### 3. Verify Required System Packages
If the bootstrap warns about missing dependencies, install them via `pacman` or your helper:
```bash
sudo pacman -S i3-wm polybar alacritty picom rofi dunst fastfetch feh redshift maim xclip xdotool
```

### 4. Restart Desktop Session
Reload your window manager configuration using **`Mod+Shift+r`** to apply the settings.

---

## 🎯 Modular i3 Keyboard Shortcuts

| Shortcut Bind | Action Executed |
| :--- | :--- |
| **`Mod + Return`** | Opens an Alacritty terminal container |
| **`Mod + d`** | Launches the Rofi application search menu |
| **`Mod + Shift + q`** | Closes the focused window |
| **`Mod + l`** | Triggers the frosted glass system locker |
| **`Mod + g`** | Toggles gaps on/off dynamically |
| **`Mod + /`** | Cycles floating shortcut guides |
| **`Mod + Shift + n`** | Toggles Redshift night-light filter |
| **`Mod + Shift + v`** | Toggles the V.E.N.U.S. cybernetic assistant widget |
