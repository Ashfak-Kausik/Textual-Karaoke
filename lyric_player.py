import re
import time
import sys
from colorama import Fore, Style, init
init(autoreset=True)

# -------- SETTINGS --------
LRC_FILE = "Pal Pal (with Talwiinder) - Afusic.lrc"
MODE = "romantic"  # choose: "heartbreak", "dance", "romantic"
# --------------------------

def type_effect(text, speed=0.05):
    """Print text with a typewriter-like effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def parse_lrc(file_path):
    """Parse an .lrc file and return list of (time_in_seconds, lyric_line)"""
    pattern = r"\[(\d+):(\d+\.\d+)\](.*)"
    lyrics = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            match = re.match(pattern, line.strip())
            if match:
                minute, second, text = match.groups()
                total_time = float(minute) * 60 + float(second)
                lyrics.append((total_time, text.strip()))
    return lyrics

def get_style(text):
    return text  # disable colors for clean output

def play_lyrics(lyrics):
    """Play lyrics in sync with timestamps."""
    if not lyrics:
        print("No lyrics found in LRC file.")
        return
    
    start_time = time.time()
    for i, (lyric_time, text) in enumerate(lyrics):
        now = time.time() - start_time
        wait = lyric_time - now
        if wait > 0:
            time.sleep(wait)
        
        styled_text = get_style(text)
        
        # Slower typing for heartbreak, faster for dance
        if MODE == "heartbreak":
            type_effect(styled_text, speed=0.08)
        elif MODE == "dance":
            type_effect(styled_text, speed=0.02)
        else:  # romantic
            type_effect(styled_text, speed=0.04)

if __name__ == "__main__":
    lyrics = parse_lrc(LRC_FILE)
    print(Fore.YELLOW + "\n🎶 Starting Lyrics Player... 🎶\n" + Style.RESET_ALL)
    play_lyrics(lyrics)
    print(Fore.GREEN + "\n✨ Song Ended ✨" + Style.RESET_ALL)