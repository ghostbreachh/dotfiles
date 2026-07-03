#!/usr/bin/env python3
import os
import glob

firefox_dirs = [
    os.path.expanduser("~/.config/mozilla/firefox"),
    os.path.expanduser("~/.mozilla/firefox")
]

firefox_dir = None
for path in firefox_dirs:
    if os.path.exists(path):
        firefox_dir = path
        break

if not firefox_dir:
    print("Error: Firefox directory not found under ~/.config/mozilla/firefox or ~/.mozilla/firefox!")
    print("Please open Firefox once in your GUI, close it, and then run this script again.")
    exit(1)

# Find default release profile folder
profiles = glob.glob(os.path.join(firefox_dir, "*.default-release"))
if not profiles:
    profiles = glob.glob(os.path.join(firefox_dir, "*.default"))
    
if not profiles:
    print("Error: Could not find any default Firefox profile.")
    print("Please open Firefox once in your GUI, close it, and then run this script again.")
    exit(1)

profile_path = profiles[0]
print(f"Found Firefox Profile: {profile_path}")

# Create chrome directory
chrome_path = os.path.join(profile_path, "chrome")
os.makedirs(chrome_path, exist_ok=True)

# Write user.js (Telemetry blocker & custom style activator)
user_js_path = os.path.join(profile_path, "user.js")
user_js_content = f"""// Enable userChrome.css custom styles
user_pref("toolkit.legacyUserProfileCustomizations.stylesheets", true);

// Disable Pocket, telemetry, homepage bloat
user_pref("browser.startup.homepage", "file://{os.path.expanduser('~/startpage/index.html')}");
user_pref("browser.newtabpage.enabled", false);
user_pref("browser.pocket.enabled", false);
user_pref("datareporting.healthreport.uploadEnabled", false);
user_pref("browser.tabs.firefox-view", false);
user_pref("browser.toolbars.keyboard_navigation", true);
"""


with open(user_js_path, "w") as f:
    f.write(user_js_content)
print("Created user.js privacy & performance profile.")

# Write userChrome.css
user_chrome_path = os.path.join(chrome_path, "userChrome.css")
user_chrome_content = """/* Minimalist Dark Purple Firefox Theme with Floating Pill Tabs */
:root {
    --toolbar-bgcolor: #050209 !important;
    --lwt-accent-color-inactive: #160e22 !important;
    --lwt-accent-color: #050209 !important;
    --lwt-text-color: #ebd9fc !important;
    
    --autocomplete-popup-background: #050209 !important;
    --input-bgcolor: #160e22 !important;
    --input-color: #ebd9fc !important;
    --input-border-color: #9f52f0 !important;
}

/* Color tabs and main toolbar */
#navigator-toolbox {
    background-color: #050209 !important;
    border-bottom: 1px solid rgba(159, 82, 240, 0.3) !important;
}

/* Round and glow the URL address bar */
#urlbar {
    border-radius: 20px !important;
    border: 1px solid rgba(159, 82, 240, 0.3) !important;
    background-color: #160e22 !important;
    box-shadow: none !important;
}

#urlbar-background {
    background-color: #160e22 !important;
    border-radius: 20px !important;
}

/* Floating Pill Tabs Layout */
.tabbrowser-tab {
    padding-inline: 4px !important;
}

.tab-background {
    border-radius: 20px !important;
    margin-block: 4px !important;
    border: 1px solid transparent !important;
    transition: all 0.25s ease !important;
    background-image: none !important;
}

/* Active tab: Glowing purple pill */
.tabbrowser-tab[selected="true"] .tab-background {
    background-color: #160e22 !important;
    border: 1px solid #9f52f0 !important;
    box-shadow: 0 0 10px rgba(159, 82, 240, 0.2) !important;
}

/* Hovered tab: Subtle purple border */
.tabbrowser-tab:hover:not([selected="true"]) .tab-background {
    background-color: rgba(26, 18, 38, 0.4) !important;
    border: 1px solid rgba(159, 82, 240, 0.2) !important;
}

/* Hide default tab line separators */
.tab-stack {
    border: none !important;
}
.tabbrowser-tab::before,
.tabbrowser-tab::after {
    display: none !important;
}
"""

with open(user_chrome_path, "w") as f:
    f.write(user_chrome_content)
print("Created userChrome.css stylesheet theme.")
print("\n--- Firefox Ricing Complete! ---")
print("Open or restart Firefox in your GUI to see your new majestic purple aesthetic.")
