#!/usr/bin/env python3
# Advanced i3status JSON wrapper to render pill-shaped floating status blocks
# Robust stream parsing that handles leading/trailing commas correctly.

import sys
import json
import subprocess

def main():
    # Start i3status in JSON mode
    proc = subprocess.Popen(['i3status', '-c', os.path.expanduser('~/.config/i3status/config')], 
                            stdout=subprocess.PIPE, 
                            stderr=subprocess.DEVNULL, 
                            text=True)

    # Read and pass the first two lines (header and open bracket)
    try:
        header = proc.stdout.readline().strip()
        print(header)
        sys.stdout.flush()

        open_bracket = proc.stdout.readline().strip()
        print(open_bracket)
        sys.stdout.flush()
    except Exception:
        sys.exit(1)

    while True:
        try:
            line = proc.stdout.readline().strip()
            if not line:
                break
            
            # Detect comma positions to preserve stream syntax
            starts_with_comma = line.startswith(',')
            
            # Strip both leading and trailing commas for clean JSON parsing
            clean_line = line
            if clean_line.startswith(','):
                clean_line = clean_line[1:]
            if clean_line.endswith(','):
                clean_line = clean_line[:-1]
            clean_line = clean_line.strip()
            
            try:
                blocks = json.loads(clean_line)
            except json.JSONDecodeError:
                # Output raw line if it fails to parse
                print(line)
                sys.stdout.flush()
                continue

            # Check Redshift status
            is_night = False
            try:
                subprocess.run(['pgrep', '-x', 'redshift'], stdout=subprocess.DEVNULL, check=True)
                is_night = True
            except subprocess.CalledProcessError:
                pass

            # Create custom Redshift block
            redshift_text = " 󰛨  Night " if is_night else " 󰛩  Day "
            redshift_color = "#9f52f0" if is_night else "#a38db8"
            
            rs_block = {
                "name": "redshift",
                "full_text": redshift_text,
                "color": redshift_color,
                "background": "#160e22",
                "border": "#9f52f0",
                "border_top": 1,
                "border_bottom": 1,
                "border_left": 1,
                "border_right": 1,
                "separator": False,
                "separator_block_width": 12
            }

            # Format and theme all other blocks
            themed_blocks = [rs_block]
            for b in blocks:
                if not b.get("full_text"):
                    continue
                
                # Apply pill styling parameters
                b["background"] = "#160e22"
                b["border"] = "#9f52f0"
                b["border_top"] = 1
                b["border_bottom"] = 1
                b["border_left"] = 1
                b["border_right"] = 1
                b["separator"] = False
                b["separator_block_width"] = 12
                
                # Pad text slightly for a cleaner look
                b["full_text"] = f" {b['full_text'].strip()} "
                
                themed_blocks.append(b)

            # Re-serialize and restore the leading/trailing commas
            out_str = json.dumps(themed_blocks)
            if starts_with_comma:
                out_str = "," + out_str
            elif line.endswith(','):
                out_str = out_str + ","
                
            print(out_str)
            sys.stdout.flush()
        except KeyboardInterrupt:
            break
        except Exception:
            continue

if __name__ == '__main__':
    main()
